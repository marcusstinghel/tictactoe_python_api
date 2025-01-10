from abc import ABC, abstractmethod
from typing import Literal

from app.domain.entities import Game, Board, Movements
from typing import Union, List


class GameRepositoryInterface(ABC):

    @abstractmethod
    def create_game(
            self,
            player_id: int,
            board: Board,
            state: Literal['in_progress', 'finished'],
            winner: Literal[-1, 0, 1],
            movements: Union[Movements, None]
    ) -> Game:
        pass

    @abstractmethod
    def get_game(self, id: int = None) -> Game:
        pass

    @abstractmethod
    def get_in_progress_game(self, player_id: int) -> Game:
        pass

    @abstractmethod
    def get_games(self, games_amount: int) -> List[Game]:
        pass

    @abstractmethod
    def update_game(
            self,
            id: int,
            player_id: int,
            board: Board,
            state: Literal['in_progress', 'finished'],
            winner: Literal[-1, 0, 1],
            movements: Movements = None,
    ) -> Game:
        pass