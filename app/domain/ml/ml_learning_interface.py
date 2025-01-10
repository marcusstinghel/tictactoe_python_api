from abc import ABC, abstractmethod
from typing import List

from app.domain.entities import Game

class MLLearningInterface(ABC):

    @abstractmethod
    def learn(self, games: List[Game], pth_file_path: str):
        pass
