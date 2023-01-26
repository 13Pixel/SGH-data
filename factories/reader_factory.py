
from readers.bh1750_reader import BH1750SensorReader
from readers.dht22_reader import DHT22SensorReader

from enums.sensor_reader import SensorReaderType
from readers.sensor_reader import SensorReader

class SensorReaderFactory:

    @classmethod
    def create_reader(cls, type: SensorReaderType) -> SensorReader:
        if type is SensorReaderType.BH1750:
            return BH1750SensorReader()

        elif type is SensorReaderType.DHT22:
            return DHT22SensorReader()
        else:
            print(f"Error such factory doesn't exist: {type}")