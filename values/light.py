from typing import Any
import values
import time

from .sensor_value import SensorValue

class Light(SensorValue):
    def __init__(self) -> None:
        self.sensor = 'light'
        self._value = float(0)
        self.valid = True
        self.timestamp = time.time()


    @property
    def value(self):
        ## Galima bet koki formatting / converting daryti pries returninant
        return self._value


    @value.setter
    def value(self, val: Any):
        ## Galima cia nustatyti ar gauta reiksme is sensor_reader yra tinkama - not None
        ## Galima custom settinint values
        if val is None:
            print("Error wile settings Light value to None")
            self.valid = False
            return
        _value_temp = (val[1] + (256 * val[0])) / 1.2
        
        if isinstance(_value_temp, values.light.Light):
            self._value = _value_temp
        else:
            self._value = round(_value_temp, 2)