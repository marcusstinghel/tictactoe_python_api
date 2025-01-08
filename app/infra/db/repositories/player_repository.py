from sqlalchemy.orm import Session
from app.infra.db.repositories import decorators as dc
from app.infra.db.entities import Player


class PlayerRepository:
    session: Session

    @classmethod
    @dc.use_db_session
    def create_player(cls, first_name: str, last_name: str, nickname: str):
        player = Player(
            first_name=first_name,
            last_name=last_name,
            nickname=nickname
        )
        cls.session.add(player)
