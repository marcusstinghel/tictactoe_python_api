from app.domain.entities import Player


class PlayerService:
    def __init__(self, player: Player):
        self.__player = player

    @property
    def get_player(self) -> Player:
        return self.__player

    def declare_victory(self):
        self.__player.victories = self.__player.victories or 0
        self.__player.victories += 1

    def declare_defeat(self):
        self.__player.defeats = self.__player.defeats or 0
        self.__player.defeats += 1

    def declare_draw(self):
        self.__player.draws = self.__player.draws or 0
        self.__player.draws += 1
