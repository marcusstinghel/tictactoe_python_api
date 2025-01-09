from sqlalchemy.orm import Session

from app.domain.entities import Player
from app.infra.db.repositories import decorators as dc
from app.infra.db.entities import Player as PlayerDBEntity
from app.domain.repositories import PlayerRepositoryInterface


class PlayerRepository(PlayerRepositoryInterface):
    session: Session

    @classmethod
    @dc.use_db_session
    def create_player(cls, first_name: str, last_name: str, nickname: str) -> Player:
        db_player = PlayerDBEntity(
            first_name=first_name,
            last_name=last_name,
            nickname=nickname
        )
        cls.session.add(db_player)
        cls.session.commit()
        player = Player(
            id=db_player.id,
            first_name=db_player.first_name,
            last_name=db_player.last_name,
            nickname=db_player.nickname,
            victories=db_player.victories,
            defeats=db_player.defeats,
            draws=db_player.draws,
        )
        return player

    @classmethod
    @dc.use_db_session
    def get_player(cls, id: int) -> Player:
        db_player = cls.session.query(PlayerDBEntity).get(id)
        player = Player(
            id=db_player.id,
            first_name=db_player.first_name,
            last_name=db_player.last_name,
            nickname=db_player.nickname,
            victories=db_player.victories,
            defeats=db_player.defeats,
            draws=db_player.draws,
        )
        return player

    @classmethod
    @dc.use_db_session
    def update_player(cls, id: int, first_name: str, last_name: str, nickname: str, victories: int, defeats: int, draws: int) -> Player:
        db_player = cls.session.query(PlayerDBEntity).get(id)
        db_player.first_name = first_name
        db_player.last_name = last_name
        db_player.nickname = nickname
        db_player.victories = victories
        db_player.defeats = defeats
        db_player.draws = draws
        cls.session.commit()
        player = Player(
            id=db_player.id,
            first_name=db_player.first_name,
            last_name=db_player.last_name,
            nickname=db_player.nickname,
            victories=db_player.victories,
            defeats=db_player.defeats,
            draws=db_player.draws,
        )
        return player
