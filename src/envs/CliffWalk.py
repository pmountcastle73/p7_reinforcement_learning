from typing import Optional
import numpy as np
import gymnasium as gym

class CliffWalk(gym.Env):
    def __init__(self, 
        w:int, 
        h:int, 
        start:Optional[list[np.int32]]=None,
        end:Optional[list[np.int32]]=None
    ):
        self.w = w
        self.h = h
        self.action_space = gym.spaces.Discrete(4)
        self._action_to_direction = {
            0 : np.array([-1,0]),  # UP
            1 : np.array([0, 1]),  # RIGHT
            2 : np.array([1, 0]),  # DOWN
            3 : np.array([0,-1]),  # LEFT
        }
        self.start = np.array(start,dtype=np.int32) if start is not None else np.array([0,0],dtype=np.int32)
        self.end   = np.array(end,dtype=np.int32) if end is not None else np.array([w-1,h-1],dtype=np.int32)
        self._agent_location = self.start.copy()
        self._target_location = self.end.copy()
        low = np.array([0,0],dtype=np.int32)
        high = np.array([w-1,h-1],dtype=np.int32)
        self.observation_space = gym.spaces.Dict(
            {
                "agent" : gym.spaces.Box(
                    low=low,
                    high=high,
                    shape=(2,),
                    dtype=np.int32
                ),
                "target" : gym.spaces.Box(
                    low=low,
                    high=high,
                    shape=(2,),
                    dtype=np.int32
                )
            }
        )
        self.gridworld = np.zeros((grid_h,grid_w))
        for h in range(self.grid_h):
            for w in range(self. grid_w):
                if(h == 3) and (w == 0 or w ==11):
                    self.gridworld[h][w] = 0
                elif h != 3 and (w != 0 or w != 11):
                    self.gridworld[h][w] = -1
                else:
                    self.gridworld[h][w] = -100
    def _get_obs(self):
        return {"agent": self._agent_location, "target": self._target_location}
    def reset(self, seed: Optional[int] = None, options: Optional[dict] = None):
        # IMPORTANT: Must call this first to seed the random number generator
        super().reset(seed=seed)

        # Randomly place the agent anywhere on the grid
        self._agent_location = ...

        # Randomly place target, ensuring it's different from agent position
        self._target_location = ...
        while np.array_equal(self._target_location, self._agent_location):
            self._target_location = self.np_random.integers(
                0, self.size, size=2, dtype=int
            )

        observation = self._get_obs()
        info = self._get_info()

        return observation, info
    def step(self,action):
        ...
    