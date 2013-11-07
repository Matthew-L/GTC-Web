__author__ = 'Micah'

import unittest
from calculator import calculator

class MyTestCase(unittest.TestCase):
    def test_calculate_tension(self):
        calc = calculator.GTC(1, 'PL', .007, 'C', 0)
        #self.assertEqual(1, calc.calculate_tension())
        self.assertTrue(False)

    def test_convert_to_freq(self):
        calc = calculator.GTC(1, 'PL', .007, 'C', 0)
        self.assertEqual(16.352, calc.freq)
        calc = calculator.GTC(1, 'PL', .007, 'C#/Db', 0)
        self.assertEqual(17.324, calc.freq)
        calc = calculator.GTC(1, 'PL', .008, 'C#/Db', 0)
        self.assertEqual(.00001418, calc.unit_weight)
        calc = calculator.GTC(1, 'PL', .007, 'C#/Db', 0)
        self.assertEqual(.00001085, calc.unit_weight)

if __name__ == '__main__':
    unittest.main()

