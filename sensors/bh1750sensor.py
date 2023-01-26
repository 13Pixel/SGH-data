from typing import List

from sensors.sensor import Sensor

from values.sensor_value import SensorValue
from readers.sensor_reader import SensorReader

from values.light import Light

class BH1750Sensor(Sensor):

    def __init__(self, reader: SensorReader) -> None:
        super().__init__(reader)
        self.__values = [Light()]

    def get_values(self) -> List[SensorValue]:
        read_values = self.reader.read()
        self.__values[0].value = read_values
        
        return self.__values