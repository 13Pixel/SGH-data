from typing import Any
import values
import json
import time


from values.sensor_value import SensorValue

class Temperature(SensorValue):
    def __init__(self) -> None:
        self.sensor = 'temperature'
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
            print("Error wile settings Temp value to None")
            self.valid = False
            return
        
        if isinstance(val, values.temperature.Temperature):
            self._value = val
        else:
            self._value = round(val, 2)