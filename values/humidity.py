from typing import Any
import time
from values.sensor_value import SensorValue
import values

class Humidity(SensorValue):
    def __init__(self) -> None:
        self.sensor = 'humidity'
        self._value = float(0)
        self.valid = True
        self.timestamp = time.time()


    @property
    def value(self) -> str:
        ## Galima bet koki formatting / converting daryti pries returninant
        return str(self._value)


    @value.setter
    def value(self, val: Any):
        ## Galima cia nustatyti ar gauta reiksme is sensor_reader yra tinkama - not None
        if val is None:
            # print("Error wile settings Humidity value to None")
            self.valid = False
            return

        if isinstance(val, values.humidity.Humidity):
            self._value = val
        else:
            self._value = round(val, 2)

        