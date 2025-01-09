from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.infra.db.entities import Base


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String)
    nickname = Column(String, unique=True)
    victories = Column(Integer, nullable=True)
    defeats = Column(Integer, nullable=True)
    draws = Column(Integer, nullable=True)

    games = relationship('Game', back_populates='player')

    def __repr__(self):
        return f"<Player(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, nickname={self.nickname}, victories={self.victories}, defeats={self.defeats}, draws={self.draws})>"
