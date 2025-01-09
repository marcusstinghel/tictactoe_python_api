from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app.infra.db.entities.player import Player
from app.infra.db.entities.game import Game
