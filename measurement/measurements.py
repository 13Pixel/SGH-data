from json import encoder
import time
from values.humidity import Humidity
from values.light import Light
from values.temperature import Temperature
from enums.sensor_reader import SensorReaderType
from factories.reader_factory import SensorReaderFactory
from sensors.dht22sensor import DHT22Sensor
from sensors.bh1750sensor import BH1750Sensor
from encoder.values_encoder import MyEncoder

import json

class Measurements():

    def __init__(self) -> None:
        self.timestamp = time.time()
        self.__values = [Temperature(), Humidity(), Light()]

        self.readerDHT22 = SensorReaderFactory.create_reader(SensorReaderType.DHT22)
        self.readerBH1750 = SensorReaderFactory.create_reader(SensorReaderType.BH1750)

    def set_sensors_data(self):

        sensor = DHT22Sensor(self.readerDHT22)
        sensor2 = BH1750Sensor(self.readerBH1750)

        data = sensor.get_values()
        data2 = sensor2.get_values()

        self.__values[0] = data[0] 
        self.__values[1] = data[1] 
        self.__values[2] = data2[0]

        return self.__values


    def toJSON(self):
        data = json.loads(MyEncoder().encode(self.__values))
        return {"timestamp": self.timestamp, "sensors":data }
