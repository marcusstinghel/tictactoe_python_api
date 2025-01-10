from app.domain.ml import MLLearningInterface
from app.domain.repositories import GameRepositoryInterface

class MLTrainer:
    def __init__(self, ml_learning: MLLearningInterface, game_repository: GameRepositoryInterface):
        self.__ml_learning = ml_learning
        self.__game_repository = game_repository

    def train(self, games_amount: int, pth_file_path: str):
        games = self.__game_repository.get_games(games_amount)
        self.__ml_learning.learn(games=games, pth_file_path=pth_file_path)