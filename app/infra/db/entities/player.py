from sqlalchemy import Column, Integer, String

from app.infra.db.entities import Base


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String)
    nickname = Column(String, unique=True)

    def __repr__(self):
        return f"<Player(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, nickname={self.nickname})>"
