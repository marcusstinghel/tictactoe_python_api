import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.data import TensorDataset
from typing import List

from app.infra.ai.models import TictactoeNNModel
from app.infra.ai.services import DatasetCreatorService
from app.domain.entities import Game
from app.domain.ml import MLLearningInterface


class AILearning(MLLearningInterface):
    __games: List[Game]
    __pth_file_path: str
    __dataset: TensorDataset
    __model: TictactoeNNModel
    __optimizer: optim.Optimizer
    __criterion: nn.CrossEntropyLoss

    @classmethod
    def learn(cls, games: List[Game], pth_file_path: str):
        cls.__games = games
        cls.__pth_file_path = pth_file_path
        cls.__generate_dataset()
        cls.__define_model()
        cls.__define_optimizer()
        train_loader = DataLoader(cls.__dataset, batch_size=4, shuffle=True)
        epochs = 10
        for epoch in range(epochs):
            for data in train_loader:
                board, winner = data
                cls.__optimizer.zero_grad()
                output = cls.__model(board)
                loss = cls.__criterion(output, winner.long())
                loss.backward()
                cls.__optimizer.step()
        cls.__save_learning()

    @classmethod
    def __generate_dataset(cls):
        dataset_creator = DatasetCreatorService(games=cls.__games)
        cls.__dataset = dataset_creator.create_dataset()

    @classmethod
    def __define_model(cls):
        cls.__model = TictactoeNNModel()
        cls.__model.train()

    @classmethod
    def __define_optimizer(cls):
        cls.__optimizer = optim.Adam(cls.__model.parameters(), lr=0.001)
        cls.__criterion = nn.CrossEntropyLoss()

    @classmethod
    def __save_learning(cls):
        torch.save(cls.__model.state_dict(), cls.__pth_file_path)