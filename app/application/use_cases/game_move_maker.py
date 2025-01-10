from typing import Dict, Union, Literal

from app.domain.entities import Game, Movement
from app.domain.repositories import GameRepositoryInterface, PlayerRepositoryInterface
from app.domain.services import GameService, PlayerService


class GameMoveMaker:
    def __init__(self, game_repository: GameRepositoryInterface, game_service: GameService,
                 player_repository: PlayerRepositoryInterface, player_service: PlayerService):
        self.__game_repository = game_repository
        self.__game_service = game_service
        self.__player_repository = player_repository
        self.__player_service = player_service

    def make_move(self, game: Game, movement: Movement) -> Dict[str, Union[Game, str]]:
        if self.__game_service.check_move_validity(movement=movement) is False:
            return {'Message': 'Invalid movement', 'game': game}
        self.__game_service.make_move()
        updated_game = self.__game_repository.update_game(**vars(self.__game_service.get_game))
        if updated_game.state == 'finished':
            self.__update_player_stats(winner=updated_game.winner)
        return {'message': 'successfully', 'game': updated_game}

    def __update_player_stats(self, winner: Literal[-1, 0, 1]):
        if winner == 1:
            self.__player_service.declare_victory()
        elif  not winner == -1:
            self.__player_service.declare_defeat()
        else:
            self.__player_service.declare_draw()
        self.__player_repository.update_player(**vars(self.__player_service.get_player))
