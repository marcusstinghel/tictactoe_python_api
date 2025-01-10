from abc import ABC, abstractmethod
from typing import List, Literal

class MLMovementInterface(ABC):

    @abstractmethod
    def make_move(self, board: List[Literal[-1, 0, 1]]) -> int:
        pass
