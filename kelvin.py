from Temperature import Temperature
import unittest

print(Temperature)

class Test(unittest.TestCase):
    def test_celsius(self):
        self.assertEqual(Temperature(celsisu=17).kelvin,float (209.15))

    def test_fahrenheit(self):
        self.assertEqual(Temperature(fahrenheit=17).kelvin,float (264.8166666667))

    def test_kelvin(self):
        self.assertEqualself.assertEqual(Temperature(kelvin=17).kelvin,17)

    def test_noArg(self):
        self.assertEqual(Temperature(kelvin=-1).kelvin,-1)

if __name__ == '__main__':
    unittest.main()