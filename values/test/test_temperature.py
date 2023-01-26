import unittest
from values.temperature import Temperature


class TestTemperature(unittest.TestCase):
    def test_value(self):
        hum = Temperature()
        res = hum.value
        self.assertEqual(res, '0.0')
        self.assertEqual(hum.valid, True)

        hum.value = 50.445
        self.assertEqual(hum.value, '50.45')
        self.assertEqual(hum.valid, True)

        hum._value = 100
        self.assertEqual(hum.value, '100')
        self.assertEqual(hum.valid, True)

        hum.value = None
        self.assertEqual(hum.value, '100')
        self.assertEqual(hum.valid, False)





if __name__ == '__main__':
    unittest.main()
