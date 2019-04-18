# from retro import make
# import numpy as np
from models.game_state import StateTools as st


# env = make(game='SonicTheHedgehog-Genesis', state='LabyrinthZone.Act1')
# obs = env.reset()


class ReinforcementAgent:

    def __init__(self, action_fn=None, alpha=1.0, epsilon=0.05, gamma=0.8, num_training=10):
        """
        :param action_fn: function that takes a state and returns all legal actions
        :param alpha: learning rate
        :param epsilon: exploration rate
        :param gamma: discount factor
        :param num_training: number of training episodes
        """
        self.get_legal_actions = lambda state: st.get_legal_actions(state) if not action_fn else action_fn
        self.alpha = float(alpha)
        self.epsilon = float(epsilon)
        self.discount = float(gamma)
        self.numTraining = int(num_training)

    ####################################
    #    Override These Functions      #
    ####################################
    def get_q_value(self, state, action):
        """
        q_value = reward(state, action)
        """
        pass

    def get_value(self, state):
        """
        V(s) = max_{a in actions} Q(s,a)
        """
        pass

    def get_policy(self, state):
        """
        policy(s) = arg_max_{a in actions} Q(s,a)
        """
        pass

    def get_action(self, state):
        """
        state: can call state.getLegalActions()
        Choose an action and return it.
        """
        pass

    def update(self, state, action, next_state, reward):
        """
        This class will call this function after observing a transition and reward
        """
        pass


class FeatureBasedAgent(ReinforcementAgent):
    def __init__(self, *args):
        super().__init__(*args)
        self.feature_fn = self.get_feature_func()

    def get_feature_func(self):
        return {
            "position": self.position,
            "nearest_enemy": self.nearest_enemy,
            "is_underwater": self.is_underwater
        }

    def position(self):
        pass

    def nearest_enemy(self):
        pass

    def is_underwater(self):
        pass
