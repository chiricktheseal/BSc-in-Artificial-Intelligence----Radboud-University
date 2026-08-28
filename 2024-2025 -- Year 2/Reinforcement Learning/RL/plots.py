import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

ACTION_SYMBOLS = {
	0: '←',  # left
	1: '↓',  # down
	2: '→',  # right
	3: '↑'   # up
}

#------- HELPER FUNCTIONS FROM MAIN JUPYTER NOTEBOOK ---------#
def create_frozenlake_env(size=4, seed=6, is_slippery=True, render_mode=None):
	from gymnasium.envs.toy_text.frozen_lake import generate_random_map
	desc = generate_random_map(size=size, seed=seed)
	env = gym.make('FrozenLake-v1', render_mode=render_mode, desc=desc, is_slippery=is_slippery)
	return env

def mc_prediction(env, pi, max_episodes=10000, gamma=0.9):
	#Initialization
	num_states = env.observation_space.n
	v = np.zeros(num_states)
	returns = {s: [] for s in range(num_states)}
	
	# Main Loop
	for _ in range(max_episodes):  
		obs, _ = env.reset()
		episode = []
		episode_over = False
		
		# Generating an episode
		while not episode_over:
			action = pi[obs]
			next_state, reward, terminated, truncated, _ = env.step(action)
			
			episode.append((obs, action, reward))
			obs = next_state
			episode_over =  terminated or truncated
		
		G = 0.0
		for t in reversed(range(len(episode))):
			state, action, reward = episode[t]
			G = gamma*G + reward
   
			# Forward loop until t-1 to check if 'state' appears before in the episode sequence
			if not any(episode[i][0] == state for i in range(t)):
				returns[state].append(G)
	
	# The mean average of G for each state
	for s in range(num_states):
		if len(returns[s]) > 0.0:
			v[s] = np.mean(returns[s])
  
	return v
#------- HELPER FUNCTIONS FROM MAIN JUPYTER NOTEBOOK ---------#

# Printing the final policy as a 'heat map'
def print_final_policy(env, policy):
	num_states = env.observation_space.n
	size = int(np.sqrt(num_states))
	
	final_policy_reshaped = np.reshape([policy[state] for state in range(num_states)], (size, size))
	final_policy_reshaped = np.vectorize(lambda x: ['Left', 'Down', 'Right', 'Up'][x])(final_policy_reshaped)

	plt.figure(figsize=(8, 6))
	sns.heatmap(np.zeros_like(final_policy_reshaped, dtype=float),
			annot=final_policy_reshaped,
			fmt="", cmap="gray", linewidths=0.5, square=True, cbar=False)
	plt.title("Final Policy Heatmap")
	plt.xlabel("X-axis (States)")
	plt.ylabel("Y-axis (States)")
	plt.show()

def run_algorithm_and_evaluate(algorithm, algo_params, env_params={'size': 4, 'seed': 6, 'is_slippery': True}, eval_episodes=1000):
	env = create_frozenlake_env(**env_params)
	result = algorithm(env, **algo_params)
	
	# Unpack results.
	if isinstance(result, tuple):
		if len(result) == 3:
			Q, pi, episode_rewards = result
		elif len(result) == 2:
			Q, episode_rewards = result
			num_states = env.observation_space.n
			pi = {s: np.argmax(Q[s]) for s in range(num_states)}
		else:
			raise ValueError("Unexpected result format from algorithm.")
	else:
		Q = result
		num_states = env.observation_space.n
		pi = {s: np.argmax(Q[s]) for s in range(num_states)}
		episode_rewards = []
	
	# Evaluate policy using the episode rewards from training.
	recent_rewards = episode_rewards[-eval_episodes:] if len(episode_rewards) >= eval_episodes else episode_rewards
	avg_reward = np.mean(recent_rewards) if recent_rewards else None
	successes = [1 if r > 0 else 0 for r in recent_rewards]
	success_rate = np.mean(successes) if recent_rewards else None
	rolling_success = pd.Series(episode_rewards).rolling(window=100, min_periods=1).mean().tolist() if episode_rewards else None

	v_mc = mc_prediction(env, pi, max_episodes=eval_episodes)


	env.close()
	return {
		'policy': pi,
		'avg_reward': avg_reward,
		'success_rate': success_rate,
		'rolling_success': rolling_success,
		'V_mc': v_mc,
		'env': env,
	}
 
# For testing Policy and Value Iteration
def test_convergence_speed(algorithm, base_params, param_variations, env_params={'size': 4, 'seed': 6, 'is_slippery': True}):
	results = []

	for key, values in param_variations.items():
		for value in values:
			test_case = base_params.copy()
			test_case[key] = value
			test_case['label'] = f"{key}={value}"
			env = create_frozenlake_env(**env_params)
			
			v, pi, iterations = algorithm(env, **test_case)
			
			results.append({
				'label': test_case['label'],
				'iterations': iterations,
				'params': test_case
			})
			
			env.close()
			# print(f"Test {test_case['label']}: Converged in {iterations} iterations")

	groups = {}
	for res in results:
		param_name, param_value = res['label'].split("=")
		if param_name not in groups:
			groups[param_name] = {'values': [], 'iterations': []}
		groups[param_name]['values'].append(float(param_value))
		groups[param_name]['iterations'].append(res['iterations'])
	
	# Plot convergence speed for each hyperparameter.
	for param_name, data in groups.items():
		# Sort data by hyperparameter value.
		sorted_data = sorted(zip(data['values'], data['iterations']), key=lambda x: x[0])
		x_vals, y_vals = zip(*sorted_data)
		plt.figure(figsize=(8, 4))
		plt.plot(x_vals, y_vals, marker='o')
		plt.xlabel(param_name)
		plt.ylabel("Iterations to Convergence")
		plt.title(f"Convergence Speed vs {param_name}")
		plt.grid(True, alpha=0.3)
		plt.show()
	
	return pi

def test_and_compare_hyperparameters(algorithm, base_params, param_variations, env_params={'size': 4, 'seed': 6, 'is_slippery': True}, eval_episodes=100):
	test_cases = []
	
	# Create test cases for each parameter variation (vary one parameter at a time).
	for key, values in param_variations.items():
		for value in values:
			test_case = base_params.copy()
			test_case[key] = value
			test_case['label'] = f"{key}={value}"
			test_cases.append(test_case)
   
	results = []
	for case in test_cases:
		print(f"Testing: {case['label']}")
		result = run_algorithm_and_evaluate(algorithm, algo_params=case, 
											env_params=env_params, eval_episodes=eval_episodes)
		results.append({
			'label': case['label'],
			'success_rate': result['success_rate'],
			'avg_reward': result['avg_reward'],
			'rolling_success': result['rolling_success'],
			'V_mc': result['V_mc'],
			'params': case
		})
	
	# Determine best hyperparameters (print only).
	best_alpha = max([r for r in results if r['label'].startswith("alpha=")], 
					 key=lambda x: x['success_rate'] if x['success_rate'] is not None else 0, default=None)
	best_gamma = max([r for r in results if r['label'].startswith("gamma=")], 
					 key=lambda x: x['success_rate'] if x['success_rate'] is not None else 0, default=None)
	best_epsilon = max([r for r in results if r['label'].startswith("initial_epsilon=")], 
					   key=lambda x: x['success_rate'] if x['success_rate'] is not None else 0, default=None)
	
	print("\nBest hyperparameters:")
	if best_alpha is not None:
		print(f"Alpha: {best_alpha['label']} ({best_alpha['success_rate']:.2%})")
	if best_gamma is not None:
		print(f"Gamma: {best_gamma['label']} ({best_gamma['success_rate']:.2%})")
	if best_epsilon is not None:
		print(f"Initial Epsilon: {best_epsilon['label']} ({best_epsilon['success_rate']:.2%})")
	
	# Plot the rolling success curves for each hyperparameter group.
	groups = {'alpha': [], 'gamma': [], 'initial_epsilon': []}
	for r in results:
		label = r['label']
		if label.startswith("alpha="):
			groups['alpha'].append(r)
		elif label.startswith("gamma="):
			groups['gamma'].append(r)
		elif label.startswith("initial_epsilon="):
			groups['initial_epsilon'].append(r)
	
	base_color = "blue"  
	min_opacity = 0.2  
	max_opacity = 0.9  
	
	for param, group_results in groups.items():
		if group_results:
			plt.figure(figsize=(12, 5))
			num_curves = len(group_results)
			for i, r in enumerate(group_results):
				if r['rolling_success'] is not None:
					# Scale opacity within range [min_opacity, max_opacity]
					opacity_scale = min_opacity + (max_opacity - min_opacity) * (i / max(num_curves - 1, 1))
					plt.plot(r['rolling_success'], color=base_color, alpha=opacity_scale, label=r['label'])
			plt.title(f"Rolling Success Curve for {param}")
			plt.xlabel("Episode")
			plt.ylabel("Rolling Average Reward")
			plt.legend()
			plt.grid(True, alpha=0.3)
			plt.show()
	
	return results

def compare_algorithms_with_base_params(algorithms, base_params, env_params={'size': 4, 'seed': 6, 'is_slippery': True}, eval_episodes=100):
	algo_names = []
	state_values = [] 
	
	for alg in algorithms:
		if alg.__name__ == "random_policy":
			# Special handling for random_policy
			env = create_frozenlake_env(**env_params)
			pi = alg(env)
   
			v_mc = mc_prediction(env, pi, max_episodes=eval_episodes)

			result = {'policy': pi, 'V_mc': v_mc, 'env': env}
   
			print(f"Final Policy for {alg.__name__}:")
			print_final_policy(env, pi)
			env.close()
		else:
			# For all other algorithms, use run_algorithm_and_evaluate.
			result = run_algorithm_and_evaluate(alg, algo_params=base_params, env_params=env_params, eval_episodes=eval_episodes)
			print(f"Final Policy for {alg.__name__}:")
			print_final_policy(result['env'], result['policy'])
		print("-" * 40)
		
		# Use the MC prediction value function (V_mc)
		if result['V_mc'] is not None:
			state_values.append(result['V_mc'])
		else:
			state_values.append(None)
		algo_names.append(alg.__name__)
	
	# Filter out algorithms with no valid V_mc data.
	valid = [(name, val) for name, val in zip(algo_names, state_values) if val is not None]
	if not valid:
		print("No valid MC prediction data available for comparison.")
		return
	
	names, values = zip(*valid)
	num_states = len(values[0])
	x = np.arange(num_states)  # state indices on x-axis
	width = 0.8 / len(names) 
	
	plt.figure(figsize=(12, 6))
	for i, (name, v) in enumerate(zip(names, values)):
		plt.bar(x + i * width, v, width=width, label=name)
	
	plt.title("MC-Predicted State Values for Each Algorithm")
	plt.xlabel("State Index")
	plt.ylabel("Estimated Value")
	plt.xticks(x + width * (len(names) - 1) / 2, x)
	plt.legend()
	plt.grid(True, axis='y', alpha=0.3)
	plt.show()
  

# Parameters for comparison (the main parameter changes, the rest are fixed)
base_params = {
	'alpha': 0.1,
	'gamma': 0.95,
	'max_episodes': 1000,
	'initial_epsilon': 0.5
}


# Hyperparameter variations for Policy and Value Iteration
param_variations_vpi = {
	'gamma':   [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99],
	'theta':   [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99],
}

# Hyperparameter variations for Monte Carlo Control
param_variations_mc = {
	'gamma':   [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99]
}

# Hyperparameter variations for Temporal Difference Algorithms
param_variations_td = {
	'alpha':   [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99],
	'gamma':   [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99],
	'initial_epsilon': [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99]
}
