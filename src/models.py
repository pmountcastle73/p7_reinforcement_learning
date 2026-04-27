import numpy as np
import gymnasium as gym
from gymnasium.spaces import Space
from collections import defaultdict

class Qlearner:
    def __init__(self,A:Space,a:float=0.2,g:float=0.80,e:float=0.2):
        self.A = A
        self.a = a
        self.g = g
        self.e = e
        self.Q = defaultdict(lambda : np.zeros(A.n))
    def act(self,s):
        s = str(s)
        if np.random.uniform() < self.e:
            return self.A.sample()
        return np.random.choice(np.flatnonzero(self.Q[s] == self.Q[s].max()))
    def update_Q(self,s,s_,Ai,R,terminated,Ai_=None):
        s,s_ = str(s), str(s_)
        self.Q[s][Ai] += self.a * (R + self.g * np.max(self.Q[s_]) * (not terminated) - self.Q[s][Ai])

class SARSA(Qlearner):
    def update_Q(self,s,s_,Ai,R,terminated,Ai_):
        s,s_ = str(s), str(s_)
        self.Q[s][Ai] += self.a * (R + self.g * self.Q[s_][Ai_] * (not terminated) - self.Q[s][Ai])

class eSARSA(SARSA):
    def update_Q(self,s,s_,Ai,R,terminated,Ai_):
        s,s_ = str(s), str(s_)
        Eq   = 0
        
        nG   = np.sum(np.flatnonzero(self.Q[s_,:] == self.Q[s_,:].max()))
    
        for Ai in range(self.A.n):
            if self.Q[s_][Ai] ==  self.Q[s_,:].max():
                P = self.e / self.A.n
            else:
                P = (1 - self.e) / nG + self.e / self.A.n
            Eq += self.Q[s_][Ai] * P

        self.Q[s][Ai] += self.a * (R + self.g * Eq * (not terminated) - self.Q[s][Ai])
