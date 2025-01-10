from app.domain.entities import Game
from app.domain.repositories import GameRepositoryInterface


class GameStarter:
    def __init__(self, game_repository: GameRepositoryInterface):
        self.__game_repository = game_repository

    def start(self, player_id: int) -> Game:
        registered_game = self.__game_repository.create_game(
            player_id=player_id,
            board=([0, 0, 0], [0, 0, 0], [0, 0, 0]),
            state='in_progress',
            winner=0,
            movements=None,
        )
        return registered_game

