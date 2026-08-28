import gymnasium as gym
from gymnasium import envs
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import numpy as np
import random
import time


# Create the FrozenLake environment
env = gym.make('FrozenLake-v1', render_mode=None, desc=generate_random_map(size=3), is_slippery=True)
# Random map: desc=generate_random_map(size=8)

# Reset the environment to start
obs, info = env.reset()

# Display the initial state
print ("Initial Observation:", obs)

steps = 0
episode_over = False

num_states = env.observation_space.n
num_actions = env.action_space.n

pi = {}

# Deterministic random policy -- Stores only action
for s in range(num_states):
    a = env.action_space.sample()
    pi[s] = a
    

# Render mode is 'human' to view the final policy
def run_policy(policy):
    preview_env = gym.make('FrozenLake-v1', render_mode="human", desc=env.unwrapped.desc, is_slippery=True)
    total_steps = 0
    episode_over = False
        
    obs, _ = preview_env.reset()
    
    while not episode_over:
        preview_env.render()
        action = policy[obs]
        _, _, terminated, truncated, _ = preview_env.step(action)
        
        total_steps += 1
        episode_over =  terminated or truncated
     
    preview_env.close()    
    return total_steps

def epsilon_greedy(Q, state, epsilon=0.1):
    # Exploration
    if random.random() < epsilon:
        return env.action_space.sample()
    # Exploitation
    else:
        return np.argmax(Q[state])       
    

# TD Prediction: TD(0) for state-value
def TD_zero(pi, alpha, max_episodes, gamma=0.9):
    v = np.zeros(num_states)
            
    for _ in range(max_episodes):
        s, _ = env.reset()
        episode_over = False
        
        while not episode_over:
            action = pi[s]
            next_state, reward, terminated, truncated, _ = env.step(action)
            
            v[s] = v[s] + alpha * (reward + gamma*v[next_state] - v[s])
            
            s = next_state
            episode_over =  terminated or truncated       
        
    return v

# TD Prediction: TD(0) for ACTION-value
def TD_zero_action_values(pi, alpha, max_episodes, gamma=0.9):
    Q = np.zeros((num_states, num_actions))  
            
    for _ in range(max_episodes):
        s, _ = env.reset()
        episode_over = False
        
        while not episode_over:
            action = pi[s]
            next_state, reward, terminated, truncated, _ = env.step(action)
            next_action = np.argmax(Q[next_state])   
            
            Q[s][action] += alpha * (reward + gamma*Q[next_state][next_action] - Q[s][action]) # Update Q-values
            
            s = next_state
            episode_over = terminated or truncated       
    return Q


# On-policy TD Control algorithm: Sarsa
def TD_control(max_episodes, alpha=0.1, gamma=0.9, initial_epsilon=0.1, min_epsilon=0.01):
    Q = np.zeros((num_states, num_actions))
    episode_rewards = []
    epsilon = initial_epsilon

    for episode in range(max_episodes):  
        #epsilon = max(min_epsilon, initial_epsilon * (1 - episode/max_episodes)) # Epsilon linear attenuation - decreasing ε overtime has a higher chance to converge
        
        s, _ = env.reset()
        action = epsilon_greedy(Q, s, epsilon)
        total_reward = 0
        episode_over = False
        
        while not episode_over:
            next_state, reward, terminated, truncated, _ = env.step(action)
            next_action = epsilon_greedy(Q, next_state, epsilon)
            
            Q[s][action] = Q[s][action] + alpha*(reward + gamma*Q[next_state][next_action] - Q[s][action])
            
            s = next_state
            action = next_action
            
            total_reward += reward
            episode_over =  terminated or truncated  
            
        episode_rewards.append(total_reward)

    return Q, episode_rewards
    

# 2 Off-policy TD Control algorithm: Q-learning 

def Q_learning(max_episodes=1000, alpha=0.1, gamma=0.9, initial_epsilon=0.5, min_epsilon=0.01):
    Q = np.zeros((num_states, num_actions))  
    episode_rewards = []
    epsilon = initial_epsilon
    
    for episode  in range(max_episodes):
        #epsilon = max(min_epsilon, initial_epsilon * (1 - episode/max_episodes)) # Bonus - decreasing ε overtime has a higher chance to converge

        s, _ = env.reset()
        total_reward = 0
        episode_over = False

        while not episode_over:
            action = epsilon_greedy(Q, s, epsilon)
            next_state, reward, terminated, truncated, _ = env.step(action)
            
            # Q-learning update            
            Q[s][action] = Q[s][action] + alpha * (reward + gamma * np.max(Q[next_state]) - Q[s][action])
            
            s = next_state
            
            total_reward += reward
            episode_over = terminated or truncated  
            
        episode_rewards.append(total_reward)
    
    return Q, episode_rewards


#v_td_zero = TD_zero(pi, 0.1, 1000, 0.9)
#print(v_td_zero)

#Q_td_zero = TD_zero_action_values(pi, alpha=0.1, max_episodes=5000, gamma=0.99)
#print("TD(0) Action-Values (Q-table):")
#print(Q_td_zero)

#Q_sarsa, sarsa_rewards = TD_control(1000)
#final_policy = np.argmax(Q_sarsa, axis=1)
#print(final_policy)
#run_policy(final_policy)

#Run Q-learning
Q_learn, ql_rewards = Q_learning(max_episodes=5000, alpha=0.2, gamma=0.95, initial_epsilon=0.3)
print("Final Q-table:")
print(Q_learn)
final_policy = np.argmax(Q_learn, axis=1) #final policy (greedy based on Q-values)
print("Final Policy:")
print(final_policy)

run_policy(final_policy)

# total_steps = run_policy()
# print(v)
# print(pi)
# print(f"Has taken {total_steps} to die or reach goal state")




#---------------TEST--------------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def test_and_compare_hyperparameters():
    # Parameters for comparison (the main parameter changes, the rest are fixed)
    base_params = {
        'alpha': 0.1,
        'gamma': 0.95,
        'epsilon': 0.1,
        'max_episodes': 2000
    }
    
    # Creating options for each parameter
    param_variations = {
        'alpha':   [0.02, 0.1,   0.3],
        'gamma':   [0.8,  0.95,  0.99],
        'epsilon': [0.01, 0.3,   0.5]
    }
    
    test_cases = []
    
    # Alpha variations (fixed gamma and epsilon)
    for alpha in param_variations['alpha']:
        test_cases.append({
            **base_params,
            'alpha': alpha,
            'label': f"α={alpha}"
        })
    
    for gamma in param_variations['gamma']:
        test_cases.append({
            **base_params,
            'gamma': gamma,
            'label': f"γ={gamma}"
        })
    
    for epsilon in param_variations['epsilon']:
        test_cases.append({
            **base_params,
            'epsilon': epsilon,
            'label': f"ε={epsilon}"
        })
    
    results = []
    for case in test_cases:
        print(f"Testing: {case['label']}")
        Q, rewards = Q_learning(
            max_episodes=case['max_episodes'],
            alpha=case['alpha'],
            gamma=case['gamma'],
            initial_epsilon=case['epsilon']
        )
        
        successes = [1 if r > 0 else 0 for r in rewards] #1 if reached the goal
        rolling_success = pd.Series(successes).rolling(100).mean().tolist() #to prevent errors; similar to mean
        
        results.append({
            'label': case['label'],
            'rolling_success': rolling_success,
            'final_success_rate': np.mean(successes[-100:]),
            'params': case
        })
    
    return results

def plot_hyperparameter_result(results):
    plt.figure(figsize=(14, 8))
    
    alpha_cases = [r for r in results if 'α=' in r['label']]
    gamma_cases = [r for r in results if 'γ=' in r['label']]
    epsilon_cases = [r for r in results if 'ε=' in r['label']]
    
    
    plt.figure(figsize=(12, 5))
    for case in alpha_cases:
        plt.plot(case['rolling_success'], label=case['label'])
    plt.title("Learning rate (α)\nif γ=0.95, ε=0.1")
    plt.xlabel("Episode")
    plt.ylabel("Success Rate")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    
    plt.figure(figsize=(12, 5))
    for case in gamma_cases:
        plt.plot(case['rolling_success'], label=case['label'])
    plt.title("Discount factor (γ)\nпif α=0.1, ε=0.1")
    plt.xlabel("Episode")
    plt.ylabel("Success Rate")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
   
    plt.figure(figsize=(12, 5))
    for case in epsilon_cases:
        plt.plot(case['rolling_success'], label=case['label'])
    plt.title("Exploration rate (ε)\nif α=0.1, γ=0.95")
    plt.xlabel("Episode")
    plt.ylabel("Success Rate")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
   
    
    print("\nComparison of parameters (final success rate):")
    for case in results:
        print(f"{case['label']}: {case['final_success_rate']:.2%}")

results = test_and_compare_hyperparameters()
plot_hyperparameter_result(results)



best_alpha = max([r for r in results if 'α=' in r['label']], key=lambda x: x['final_success_rate'])
best_gamma = max([r for r in results if 'γ=' in r['label']], key=lambda x: x['final_success_rate'])
best_epsilon = max([r for r in results if 'ε=' in r['label']], key=lambda x: x['final_success_rate'])

print("\nBest parameteres:")
print(f"Alpha: {best_alpha['label']} ({best_alpha['final_success_rate']:.2%})")
print(f"Gamma: {best_gamma['label']} ({best_gamma['final_success_rate']:.2%})")
print(f"Epsilon: {best_epsilon['label']} ({best_epsilon['final_success_rate']:.2%})")

env.close()