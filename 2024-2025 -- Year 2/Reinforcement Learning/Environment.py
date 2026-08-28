"""
#-----Make your own environment:
import gymnasium as gym
from gymnasium import spaces
import numpy as np


#-----Create a subclass of gym.Env and implement the required methods.
class CustomEnv(gym.Env):
    def __init__(self):
        super(CustomEnv, self).__init__()
        
        self.action_space = spaces.Discrete(2)  # Two possible actions
        self.observation_space = spaces.Box(low=0, high=10, shape=(1,), dtype=np.float32)
        
        self.state = None  # Initialize state
        
    def reset (self):
        #Reset the environment to an initial state . 
        self.state = np.array([5.0])  # Example initial state
        return self.state, {}
    
    def step (self, action):
        #Apply an action and return results . 
        reward = 1 if action == 1 else 0
        self.state = self.state + (action - 0.5)
        done = self.state[0] > 10 or self.state[0] < 0
        return self.state, reward, done, False, {}
    
    def render (self):
        #Render the environment ( optional ) . 
        print(f"Current state: {self.state}")
    
    def close (self):
        #Clean up resources ( optional ) . 
        pass


#-----Register your environment to use it with Gymnasium.
#--This is necessary to be able to use your environment natively in Gymnasium.
from gymnasium . envs . registration import register

register(
    id="CustomEnv-v0",
    entry_point="__main__:CustomEnv",
)

#-----Use Gymnasium’s API to test your custom environment.
# Create the environment
env = gym.make("CustomEnv-v0")

# Interact with the environment
obs, info = env.reset()
for _ in range(10):
    action = env.action_space.sample()  # Random action
    obs, reward, done, truncated, info = env.step(action)
    env.render()
    if done:
        break
env.close()
"""



# Import Gymnasium and create FrozenLake environment
import gymnasium as gym
# Create the FrozenLake environment
env = gym.make('FrozenLake-v1', render_mode='human', desc=None, map_name="4x4", is_slippery=True)
# Reset the environment to start
obs, info = env.reset ()

# Shows the playground in the terminal
env.render() 

# Display the initial state
print ( "Initial␣Observation: ", obs )