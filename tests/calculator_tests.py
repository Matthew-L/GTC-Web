__author__ = 'Micah'

import unittest
from calculator import calculate

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

E .009" PL == 14.18#
B, .012" PL == 14.15#
G, .015" PL == 13.93#
D, .022" NW == 14.41#
A,, .030" NW == 15.17#
E,, .040 NW == 14.52#
B,,, .054 NW == 14.66#
E,,, .074 NW == 12.21#
total == 113.24#
"""


class MyTestCase(unittest.TestCase):
    def test_calculate_tension(self):
        """
        tests the tension calculation function; the values are slightly off by about +- .1 from the
        source code we based this on. This seems to be due to the way the frequencies are calculated differently

        """

        #E .009" PL == 14.18#
        calc = calculate.GTC(26.5, 'PL', .009, 'E', 4)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(14.17, tension)
        #B, .012" PL == 14.15#
        calc = calculate.GTC(26.5, 'PL', .012, 'B', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(14.14, tension)
        #G, .015" PL == 13.93#
        calc = calculate.GTC(26.5, 'PL', .015, 'G', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(13.92, tension)
        #D, .022" NW == 14.41#
        calc = calculate.GTC(26.5, 'NW', .022, 'D', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(14.39, tension)
        #A,, .030" NW == 15.17#
        calc = calculate.GTC(26.5, 'NW', .030, 'A', 2)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(15.16, tension)
        #E,, .040 NW == 14.52#
        calc = calculate.GTC(26.5, 'NW', .040, 'E', 2)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(14.50, tension)
        #B,,, .054 NW == 14.66#
        calc = calculate.GTC(26.5, 'NW', .054, 'B', 1)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(14.64, tension)
        #E,,, .074 NW == 12.21#
        calc = calculate.GTC(26.5, 'NW', .074, 'E', 1)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(12.2, tension)

        calc = calculate.GTC(25.5, 'PL', .012, 'E', 4)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(23.33, tension)

        calc = calculate.GTC(25.5, 'PL', .016, 'B', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(23.28, tension)

        calc = calculate.GTC(25.5, 'PB', .024, 'G', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(30.21, tension)

        calc = calculate.GTC(25.5, 'PB', .032, 'D', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(30.5, tension)

        calc = calculate.GTC(25.5, 'PB', .042, 'A', 2)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(29.91, tension)

        calc = calculate.GTC(25.5, 'PB', .053, 'E', 2)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(26.04, tension)

    def test_convert_to_freq(self):
        """
        tests the freq is calculated properly

        """
        calc = calculate.GTC(1, 'PL', .007, 'C', 0)
        freq = float("{0:.2f}".format(calc.freq))
        self.assertEqual(16.35, freq)

        calc = calculate.GTC(1, 'PL', .007, 'C#/Db', 0)
        freq = float("{0:.2f}".format(calc.freq))
        self.assertEqual(17.32, freq)

        calc = calculate.GTC(26.5, 'PL', .009, 'E', 4)
        freq = float("{0:.1f}".format(calc.freq))
        self.assertEqual(329.6, freq)

    def test_convert_to_unit_weight(self):
        """
        tests the unit_weight is converted properly

        """

        calc = calculate.GTC(26.5, 'NW', .074, 'G', 1)
        self.assertEqual(.00098869, calc.unit_weight)

        #G,,  .027" PL == 10.38#
        calc = calculate.GTC(25.5, 'PL', .027, 'G', 2)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(10.37, tension)
        #G,,  .060" PL == 33.08#
        calc = calculate.GTC(25.5, 'PL', .060, 'G', 2)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(33.05, tension)

        calc = calculate.GTC(1, 'PL', .008, 'C#/Db', 0)
        self.assertEqual(.00001418, calc.unit_weight)

        calc = calculate.GTC(1, 'PL', .007, 'C#/Db', 0)
        self.assertEqual(.00001085, calc.unit_weight)

        #B,  .0165" PL == 24.8#
        calc = calculate.GTC(25.5, 'PL', .0165, 'B', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(24.78, tension)




    def test_convert_to_halfsteps(self):
        """
        tests the unit_weight is converted properly

        """
        calc = calculate.GTC(1, 'PL', .008, 'C#/Db', 0)
        self.assertEqual(0, calc.convert_to_halfsteps('A', 4))
        self.assertEqual(2, calc.convert_to_halfsteps('B', 4))
        self.assertEqual(15, calc.convert_to_halfsteps('C', 6))
        self.assertEqual(-10, calc.convert_to_halfsteps('B', 3))

    def test_convert_to_unit_weight(self):
        calc = calculate.GTC(1, 'PL', .008, 'C#/Db', 0)
        wt = calc.convert_to_unit_weight('PL', .007)
        self.assertEqual(.00001085, wt)

if __name__ == '__main__':
    unittest.main()

