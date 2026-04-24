# Epsilon-Greedy QLearning 
import numpy as np

class QLearningAgent:
    def __init__(self, alpha=0.5, gamma = 1, epsilon = 0.1):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_values = None
        self.actions = None
        self.initial_state = None
        self.state = None
        self.terminal = None

    def choose_action(self):
        explore = np.random.rand()
        if explore <= self.epsilon:
            return np.random.choice(self.actions)
        else:
            x, y = self.state
            max_indexes = np.where(self.q_values[x][y] == np.max(self.q_values[x][y]))[0]
            action_idx = np.random.choice(max_indexes)
            return self.actions[action_idx]

    def reset(self):
        self.state = self.initial_state