from typing import List, Literal, Dict, Tuple

Board = Tuple[List[Literal[-1, 0, 1]], List[Literal[-1, 0, 1]], List[Literal[-1, 0, 1]]]
Movement = Dict[Literal['column', 'row', 'value'], int]
Movements = List[Movement]

from app.domain.entities.player import Player
from app.domain.entities.game import Game
