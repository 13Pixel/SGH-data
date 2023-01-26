from typing import Any
import Adafruit_DHT
from readers.sensor_reader import SensorReader

class DHT22SensorReader(SensorReader):

    SENSOR = Adafruit_DHT.DHT22
    GPIO = 4

    def __init__(self) -> None:
        super().__init__()
        
    def read(self) -> Any:
        return Adafruit_DHT.read_retry(self.SENSOR, self.GPIO)