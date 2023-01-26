import unittest
from values.humidity import Humidity


class TestHumidity(unittest.TestCase):
    def test_value(self):
        hum = Humidity()
        res = hum.value
        self.assertEqual(res, '0.0')
        self.assertEqual(hum.valid, True)

        hum.value = 50.5555
        self.assertEqual(hum.value, '50.56')
        self.assertEqual(hum.valid, True)

        hum._value = 100
        self.assertEqual(hum.value, '100')
        self.assertEqual(hum.valid, True)

        hum.value = None
        self.assertEqual(hum.value, '100')
        self.assertEqual(hum.valid, False)





if __name__ == '__main__':
    unittest.main()
