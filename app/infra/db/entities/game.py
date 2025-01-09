from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.infra.db.entities import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)
    board = Column(String, nullable=False)
    state = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    movements = Column(String, nullable=False)
    is_player_winner = Column(Boolean, nullable=False)

    player = relationship('Player', back_populates='games')

    def __repr__(self):
        return f"<Player(id={self.id}, board={self.board}, state={self.state}, player_id={self.player_id}, movements={self.movements}, is_player_winner={self.is_player_winner})>"
