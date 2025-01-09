from abc import ABC, abstractmethod

from app.domain.entities import Player


class PlayerRepositoryInterface(ABC):

    @abstractmethod
    def create_player(self, first_name: str, last_name: str, nickname: str) -> Player:
        pass

    @abstractmethod
    def get_player(self, id: int) -> Player:
        pass

    @abstractmethod
    def update_player(self, first_name: str, last_name: str, nickname: str, victories: int, defeats: int, draws: int) -> Player:
        pass
