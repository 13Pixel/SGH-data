from typing import Any
import smbus
from readers.sensor_reader import SensorReader

class BH1750SensorReader(SensorReader):

    DEVICE = 0x23
    PORT = 1
    ONE_TIME_HIGH_RES_MODE = 0x20

    def __init__(self) -> None:
        super().__init__()
        self.__bus = smbus.SMBus(self.PORT)

    def read(self) -> Any:
        return self.__bus.read_i2c_block_data(self.DEVICE, self.ONE_TIME_HIGH_RES_MODE)