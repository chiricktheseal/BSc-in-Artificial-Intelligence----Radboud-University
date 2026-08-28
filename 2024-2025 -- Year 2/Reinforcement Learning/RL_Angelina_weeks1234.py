import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import numpy as np
import time

# Create the FrozenLake environment
env = gym.make('FrozenLake-v1', render_mode="human", desc=generate_random_map(size=8), is_slippery=False)
# Random map: desc=generate_random_map(size=8)
#is_slippery=True the agent may accidentally slip into a suboptimal state, even if it chooses the correct action

# Reset the environment to start
obs, info = env.reset()

print ("Initial Observation:", obs)

steps = 0
episode_over = False

num_states = env.observation_space.n # Количество состояний (8x8 = 64)
num_actions = env.action_space.n
v = np.zeros(num_states)

states = env.observation_space #state space
actions = env.action_space #action space

theta = 0.0001 #когда изменения становятся меньше этого порога, процесс останавливается
gamma = 0.5 #агент учитывает будущие награды, но не сильно

pi = {}  # Политика (хранит действие для каждого состояния)


# Uniform random policy with p(a|s) = 0.25
# for s in range(num_states):
#     pi[s] = {a: 0.25 for a in range(4)} #агент выбирает действие случайно, и все действия равновероятны.
    
# Deterministic random policy -- Stores action:probability
# for s in range(num_states):
#     action = random.choice(range(4))
#     pi[s] = {a: (1 if a == action else 0) for a in range(4)} #выбирает одно и то же действие для данного состояния


# Deterministic random policy -- Stores only action
# Для каждого состояния s выбирается одно случайное действие и записывается в pi[s]
for s in range(num_states):
    a = env.action_space.sample()
    pi[s] = a
    # print(f"state {s}:{env.unwrapped.P[s]}")
    
    
    
    
#---------------------------------Policy Iteration---------------------------------
    
def policy_eval(pi, v, gamma, theta, num_states, env):
    delta = float('inf')

    while delta > theta:
        old_v = np.copy(v)    
        delta = 0
        
        for s in range(num_states):
            a = pi[s]  # Берём действие из текущей стратегии
            v_s = 0.0 #нов знач функции ценности для состояния s
            
            for (trans_p, next_state, reward, _) in env.unwrapped.P[s][a]: #по всем переходам из состояния s при действии a
                v_s += trans_p * (reward + gamma * old_v[next_state]) #Обновляем знач функц ценности для s с учетом награды и дисконт знач следующего состояния.
                
            v[s] = v_s #v[s] = награда + дисконт * ценность следующего состояния
            delta = max(delta, abs(v[s] - old_v[s])) #максимальным изменением значения функции ценности
            
def policy_improvement(pi, v, gamma, num_states, env):
    policy_stable = True
    
    for s in range(num_states):
        old_action = pi[s] #Сохраняем текущее действие для состояния s
        
        best_a = None
        max_action_val = float('-inf')
        
        for a in range(env.action_space.n):
            a_val = 0.0
            
            for (trans_p, next_state, reward, _) in env.unwrapped.P[s][a]: #Проходим по всем возможным переходам для действия a.
                a_val += trans_p * (reward + gamma * v[next_state])
                
            if a_val > max_action_val: #Если текущее значение действия лучше, обновляем
                max_action_val = a_val
                best_a = a
            
        pi[s] = best_a #Обновляем политику для состояния s
        
        if old_action != pi[s]: #Если действие изменилось, политика нестабильна -политика обновляется.
            policy_stable = False
            
    # Если политика не изменилась ни для одного состояния, она считается стабильной (оптимальной)
    return policy_stable
        
def policy_iteration(pi, v, gamma, theta, num_states, env, max_iter):
    for i in range(max_iter):
        policy_eval(pi, v, gamma, theta, num_states, env) #Оцениваем текущую политику.
        stable = policy_improvement(pi, v, gamma, num_states, env) #Улучшаем политику
        if stable:  #Если политика не изменилась, алгоритм завершается
            print(f"Convergence after {i+1} steps")
            break
    return v, pi



#---------------------------------Value Iteration---------------------------------

def value_iteration(v, gamma, theta, num_states, env):
    delta = float('inf')
    
    #Value Iteration-we are updating the state values (v) 
    # "What is the value of each condition if I act optimally?"
    while delta > theta:
        delta = 0
        old_v = np.copy(v)
        
        #The maximum value that can be obtained by choosing the best action is calculated.
        for s in range(num_states):
            max_action_val = float('-inf') #maximum value for the current state
            
            for a in range(num_actions):
                v_s = 0.0 #action a value for state s
                # Iterate over all possible transitions for the action
                for (trans_p, next_state, reward, _) in env.unwrapped.P[s][a]:
                    v_s += trans_p * (reward + gamma * old_v[next_state])
                
                # Update the maximum value for the current state    
                if v_s > max_action_val:
                    max_action_val = v_s   
            
            # Update the value function for the current state
            v[s] = max_action_val
            # Update delta (maximum change in value function)
            delta = max(delta, abs(v[s] - old_v[s]))
    
    # Extract the optimal policy from the optimal value function -use the already calculated values (v) to select the best actions.
    # "Which action should I choose in each state?"
    pi = {}
    #For each state s, an action is selected that maximizes the expected value.
    for s in range(num_states):
        best_a = None ## Initialize the best action and its value
        max_action_val = float('-inf')
        
        for a in range(env.action_space.n):
            v_s = 0.0
            
            # Iterate over all possible transitions for the action
            for (trans_p, next_state, reward, _) in env.unwrapped.P[s][a]:
                v_s += trans_p * (reward + gamma * v[next_state])
            
            # Update the best action
            if v_s > max_action_val:
                max_action_val = v_s
                best_a = a
        
        # Store the best action for the current state       
        pi[s] = best_a
    
    return v, pi
    
 
 
 
 
#---------------------------------On-policy, first-visit Monte Carlo Prediction---------------------------------
num_episodes = 1000

def mc_prediction_first_visit(env, pi, num_episodes, gamma):
    # Initialize value function and returns
    V = np.zeros(num_states)
    returns = {s: [] for s in range(num_states)}  # Stores returns for each state
    
    for _ in range(num_episodes):
        # Generate an episode using the policy pi
        episode_states = []
        episode_returns = []
        state = env.reset()[0]  # Reset environment and get initial state
        done = False
        
        while not done:
            action = pi[state] # Choose action according to policy
            next_state, reward, terminated, truncated, _ = env.step(action)
            episode_states.append(state)
            episode_returns.append(reward)
            state = next_state
            done = terminated or truncated
        
        # Calculate returns and update value function
        G = 0
        for t in range(len(episode_states) - 1, -1, -1):
            G = gamma * G + episode_returns[t]
            state_t = episode_states[t]
            if state_t not in episode_states[:t]: # First-visit: only update if state hasn't been visited earlier
                returns[state_t].append(G)
                V[state_t] = np.mean(returns[state_t])
    
    return V




#---------------------------------On-policy, first-visit Monte Carlo control---------------------------------
epsilon=0.1

def mc_control_first_visit(env, num_episodes, gamma, epsilon=0.1):
    # Initialize action-value function and returns
    Q = np.zeros((num_states, num_actions))
    returns = {(s, a): [] for s in range(num_states) for a in range(num_actions)}  # Stores returns for each (state, action)
    
    # Initialize policy (epsilon-greedy)
    pi = {s: np.random.choice(num_actions) for s in range(num_states)}
    
    for _ in range(num_episodes):
        # Generate an episode using the current policy pi
        episode = []
        state = env.reset()[0] # Reset environment and get initial state
        done = False
        
        while not done:
            if np.random.rand() < epsilon:  # Exploration: choose random action
                action = env.action_space.sample()
            else:  # Exploitation: choose action according to policy
                action = pi[state]
            
            next_state, reward, terminated, truncated, _ = env.step(action)
            episode.append((state, action, reward))
            state = next_state
            done = terminated or truncated
        
        # Calculate returns and update action-value function
        G = 0
        
        visited = set()  # Track visited (state, action) pairs for first-visit
        for t in range(len(episode) - 1, -1, -1):  # Loop backwards through the episode
            s, a, r = episode[t]
            G = gamma * G + r
            
            if (s, a) not in visited:  # First-visit: only update if (s, a) hasn't been visited earlier
                visited.add((s, a))
                returns[(s, a)].append(G)
                Q[s, a] = np.mean(returns[(s, a)])  # Update Q-value as the average of returns
                
                # Update policy to be greedy with respect to Q
                pi[s] = np.argmax(Q[s, :])
    
    return pi, Q
                    

#optimal_policy, optimal_value = value_iteration(v, gamma, theta, num_states, env)
#print("Optimal Value Function:", optimal_value, "\nOptimal Policy:", optimal_policy)

while not episode_over:
    steps += 1
    
    action = env.action_space.sample()  # agent policy that uses the observation and info
    #action = optimal_policy[obs] #Choose the best action based on optimal policy
    #action = int(action) 
    observation, reward, terminated, truncated, info = env.step(action)
    
    episode_over = terminated or truncated
    
    print(f"Step: {steps}, State: {observation}, Action: {action}, Reward: {reward}")
    #obs = observation #update the current state
    
    #print(env.observation_space.n)
    #print(info)
		
print(f"Has taken {steps} to die or reach goal state")

env.close()