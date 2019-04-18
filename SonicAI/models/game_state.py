from typing import Dict, Any, Callable, TypeVar


class GameState:
    def __init__(self):
        pass


class SonicGameState(GameState):
    pass


class StateTools:
    # Type variables for clarity
    Action = TypeVar("Action")
    State = TypeVar("State")
    FeatureName = TypeVar("FeatureName", str, bytes)
    FeatureFunction = Dict[FeatureName, Callable[[State], Any]]

    @staticmethod
    def get_legal_actions(state) -> Dict[Action, State]:
        """
        :return: Dictionary matching actions to their resulting state
        """
        pass

    @staticmethod
    def analyze_features(state: State, feature_fn: FeatureFunction) -> Dict[FeatureName, Any]:
        """
        :param state: The current state
        :param feature_fn: A dictionary of functions for analyzing the feature they are mapped to
        :return: Names of features mapped to their values
        """
        return {feature: func(state) for feature, func in feature_fn.values()}

