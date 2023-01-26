import unittest
from values.light import Light


class TestLight(unittest.TestCase):
    def test_value(self):
        hum = Light()
        res = hum.value
        self.assertEqual(res, 0.0)
        self.assertEqual(hum.valid, True)

        hum.value = [1, 247]
        self.assertEqual(hum.value, 419.17)
        self.assertEqual(hum.valid, True)

        hum._value = 100
        self.assertEqual(hum.value, 100)
        self.assertEqual(hum.valid, True)

        hum.value = None
        self.assertEqual(hum.value, 100)
        self.assertEqual(hum.valid, False)





if __name__ == '__main__':
    unittest.main()
