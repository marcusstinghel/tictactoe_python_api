from app.domain.entities import Player
from app.domain.repositories import PlayerRepositoryInterface


class PlayerCreator:
    def __init__(self, player_repository: PlayerRepositoryInterface):
        self.__player_repository = player_repository

    def create(self, first_name: str, last_name: str, nickname: str) -> Player:
        registered_player = self.__player_repository.create_player(
            first_name=first_name,
            last_name=last_name,
            nickname=nickname
       )
        return registered_player
