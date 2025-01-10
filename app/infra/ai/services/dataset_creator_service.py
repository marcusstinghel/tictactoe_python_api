from typing import List
from torch.utils.data import TensorDataset
import torch

from app.domain.entities import Game


class DatasetCreatorService:
    def __init__(self, games: List[Game]):
        self.__games = games

    def create_dataset(self) -> TensorDataset:
        training_data = []
        for game in self.__games:
            board = game.board[0] + game.board[1] + game.board[2]
            data = {
                'board': board,
                'movements': game.movements,
                'winner': game.winner
            }
            training_data.append(data)

            X = torch.tensor([data['board'] for data in training_data], dtype=torch.float32)
            y = torch.tensor([data['winner'] for data in training_data], dtype=torch.float32)

            dataset = TensorDataset(X, y)
            return dataset
