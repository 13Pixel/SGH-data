from typing import Any
from abc import ABC, abstractmethod

class SensorValue(ABC):

    @property
    @abstractmethod
    def value(self):
        pass

    @value.setter
    @abstractmethod
    def value(self, val):
        pass
    
    

    