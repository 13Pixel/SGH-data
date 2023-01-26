from sensors.sensor import Sensor
from values.sensor_value import SensorValue
from values.temperature import Temperature
from values.humidity import Humidity

from readers.sensor_reader import SensorReader

from typing import List

class DHT22Sensor(Sensor):

    def __init__(self, reader: SensorReader) -> None:
        super().__init__(reader)
        self.__values = [Humidity(), Temperature()]

    def get_values(self) -> List[SensorValue]:
        read_values = self.reader.read()

        for i, value in enumerate(read_values):
            self.__values[i].value = value
        
        return self.__values