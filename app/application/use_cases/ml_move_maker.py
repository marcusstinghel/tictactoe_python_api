# pega o game em questão no banco
# Trata o board de forma que ele possa usar
# usa ai_movement para dedusir uma movimentação
# retorna a movimentação escolhida

from typing import List, Literal

from app.domain.entities import Game
from app.domain.ml import MLMovementInterface
from app.domain.repositories import GameRepositoryInterface


class MLMoveMaker:
    __game_repository: GameRepositoryInterface
    __ml_movement: MLMovementInterface
    __game: Game
    __formatted_board: List[Literal[-1, 0, 1]]

    def __init__(self, game_repository: GameRepositoryInterface, ml_movement: MLMovementInterface):
        self.__game_repository = game_repository
        self.__ml_movement = ml_movement

    def make_move(self, player_id: int) -> int:
        self.__game = self.__game_repository.get_in_progress_game(player_id=player_id)
        self.__format_board()
        return self.__ml_movement.make_move(board=self.__formatted_board)

    def __format_board(self):
        self.__formatted_board = self.__game.board[0] + self.__game.board[1] + self.__game.board[2]
