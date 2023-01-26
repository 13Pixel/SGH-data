from abc import ABC, abstractmethod
from values.sensor_value import SensorValue
from readers.sensor_reader import SensorReader

from typing import List

class Sensor(ABC):
    def __init__(self, reader: SensorReader) -> None:
        self.reader = reader
        
    @abstractmethod
    def get_values(self) -> List[SensorValue]:
        pass