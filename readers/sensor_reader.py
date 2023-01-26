from typing import Any
from abc import ABC, abstractmethod

class SensorReader(ABC):

    @abstractmethod
    def read(self) -> Any:
        pass