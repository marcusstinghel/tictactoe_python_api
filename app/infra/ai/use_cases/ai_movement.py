import torch
from typing import List, Literal

from app.domain.ml import MLMovementInterface
from app.infra.ai.models import TictactoeNNModel
from app.infra.settings import EnvVarsHandler

class AIMovement (MLMovementInterface):
    __board: List[Literal[-1, 0, 1]]
    __pth_file: str
    __model: TictactoeNNModel
    __board_tensor: torch.Tensor
    __output: torch.Tensor

    @classmethod
    def make_move(cls, board: List[Literal[-1, 0, 1]]) -> int:
        cls.__board = board
        cls.__pth_file = EnvVarsHandler.get_ml_pth_file_path()
        cls.__load_saved_model()
        cls.__transform_board_to_tensor()
        cls.__make_model_prediction()
        return cls.__obtain_best_move()

    @classmethod
    def __load_saved_model(cls):
        cls.__model = TictactoeNNModel()
        cls.__model.load_state_dict(
            torch.load(cls.__pth_file, weights_only=True))
        cls.__model.eval()

    @classmethod
    def __transform_board_to_tensor(cls):
        cls.__board_tensor = torch.tensor(cls.__board, dtype=torch.float32).unsqueeze(0)

    @classmethod
    def __make_model_prediction(cls):
        with torch.no_grad():
            cls.__output = cls.__model(cls.__board_tensor)

    @classmethod
    def __obtain_best_move(cls):
        move_probabilities = cls.__output.squeeze(0).numpy()
        available_positions = [i for i in range(len(cls.__board)) if cls.__board[i] == 0]
        available_probabilities = [(i, move_probabilities[i]) for i in available_positions]
        if available_probabilities:
            move = max(available_probabilities, key=lambda x: x[1])[0]
        else:
            move = None
        return move

