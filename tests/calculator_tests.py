__author__ = 'Micah'

import unittest
from calculator import calculator

"""
source code values used for comparison
len 25.5"

E   .012" PL == 23.35#
B,  .016" PL == 23.3#
G,  .024" PB == 30.24#
D,  .032" PB == 30.53#
A,, .042" PB == 29.94#
E,, .053" PB == 26.06#
total == 163.42#

E    23#  PL == 0.0119"
B,   23#  PL == 0.0159"
G,   30#  PB == 0.0239"
D,   30#  PB == 0.0317"
A,,  30#  PB == 0.042"
E,,  26#  PB == 0.0529"
"""


class MyTestCase(unittest.TestCase):
    def test_calculate_tension(self):
        """
        tests the tension calculation function; the values are slightly off by about +- .1 from the
        source code we based this on. This seems to be due to the way the frequencies are calculated differently

        """
        calc = calculator.GTC(25.5, 'PL', .012, 'E', 4)
        self.assertEqual(23.33, calc.calculate_tension())

        calc = calculator.GTC(25.5, 'PL', .016, 'B', 3)
        self.assertEqual(23.28, calc.calculate_tension())

        calc = calculator.GTC(25.5, 'PB', .024, 'G', 3)
        self.assertEqual(30.21, calc.calculate_tension())

        calc = calculator.GTC(25.5, 'PB', .032, 'D', 3)
        self.assertEqual(30.5, calc.calculate_tension())

        calc = calculator.GTC(25.5, 'PB', .043, 'A', 2)
        self.assertEqual(29.91, calc.calculate_tension())

        calc = calculator.GTC(25.5, 'PB', .053, 'E', 2)
        self.assertEqual(26.04, calc.calculate_tension())

    def test_convert_to_freq(self):
        """
        tests the freq is calculated properly

        """
        calc = calculator.GTC(1, 'PL', .007, 'C', 0)
        self.assertEqual(16.352, calc.freq)
        calc = calculator.GTC(1, 'PL', .007, 'C#/Db', 0)
        self.assertEqual(17.324, calc.freq)

    def test_convert_to_unit_weight(self):
        """
        tests the unit_weight is converted properly

        """
        calc = calculator.GTC(1, 'PL', .008, 'C#/Db', 0)
        self.assertEqual(.00001418, calc.unit_weight)

        calc = calculator.GTC(1, 'PL', .007, 'C#/Db', 0)
        self.assertEqual(.00001085, calc.unit_weight)


if __name__ == '__main__':
    unittest.main()

