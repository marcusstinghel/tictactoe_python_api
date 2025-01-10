from typing import Literal
from app.domain.entities import Board, Movements


class Game:
    player_id: int
    board: Board
    movements: Movements

    def __init__(
            self,
            id: int,
            state: Literal['in_progress', 'finished'],
            player_id: int,
            movements: Movements,
            winner: Literal[-1, 0, 1],
            board: Board,
    ):
        self.id = id
        self.board = board
        self.state = state
        self.player_id = player_id
        self.movements = movements
        self.winner = winner

    def __repr__(self):
        return f"Game(id={self.id}, board={self.board}, state={self.state}, player_id={self.player_id}, movements={self.movements}, winner={self.winner})"
