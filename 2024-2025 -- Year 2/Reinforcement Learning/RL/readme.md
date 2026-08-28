# Reinforcement Learning Project

## Project Files
- **`RL_Algorithms.ipynb` (1)**
- **`plots.py` (2)**

## **1. RL_Algorithms.ipynb**
The first file (1), is a jupyter notebook, consisting of the code for the following algorithms and/or policy creation methods:

### **Policy-Based Methods**
- Random Policy Generation
- **Policy Iteration**
  - Policy Evaluation
  - Policy Improvement
- Value Iteration

### **Monte Carlo Methods**
- Monte Carlo Prediction
- Monte Carlo Control - With Exploring Starts

### **Temporal Difference (TD) Methods**
- TD(0)
- **On-Policy TD Control** - SARSA
- **Off-Policy TD Control** - QLearning

Each category of algorithm is separated in its own code block. The final code block contains the methods for running the algorithms and generating meaningful data and plots. To use this Jupyter notebook it is required to first install the necessary dependencies, using: 
```bash
pip install -r requirements.txt
```
## Running the Jupyter Notebook
To execute all code blocks in the notebook:
1. Open `RL_Algorithms.ipynb` in Jupyter Notebook.
2. Click **"Run" → "Run All"** from the menu bar.
3. Alternatively, press `Shift + Enter` to execute cells one by one.

### Note
It should, however, be noted that even if we use the same seed on the environment, the results will never be the same due to the algorithms' non-deterministic behaviour (MC and TD). The results/plots mentioned and displayed in the report will be with the current (initial) result in the Jupyter notebook, as delivered in the .zip folder. If you run all of it again, the results/plots may slightly vary, but they should be generally similar.

## **2. plots.py**
The second file (2) contains the code for plotting the data of the experiments. Here, we run the different algorithms with different hyperparameters and plot and compare their results. We have decided to separate this logic from the main Jupyter notebook, as it is uninteresting and not 'important' for the project / course material.
