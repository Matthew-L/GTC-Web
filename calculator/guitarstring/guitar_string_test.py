import unittest
from calculator.guitarstring.guitar_string import GuitarString, InvalidScaleLengthError, OutOfRangeError, \
    InvalidNoteError, InvalidStringMaterialError, InvalidOctaveError, InvalidGaugeError
# from .guitar_string import GuitarString
"""
source code values used for comparison
len 25.5"

E   .012" DAPL == 23.35#
B,  .016" DAPL == 23.3#
G,  .024" DAPB == 30.24#
D,  .032" DAPB == 30.53#
A,, .042" DAPB == 29.94#
E,, .053" DAPB == 26.06#
total == 163.42#

E    23#  DAPL == 0.0119"
B,   23#  DAPL == 0.0159"
G,   30#  DAPB == 0.0239"
D,   30#  DAPB == 0.0317"
A,,  30#  DAPB == 0.042"
E,,  26#  DAPB == 0.0529"

E .009" DAPL == 14.18#
B, .012" DAPL == 14.15#
G, .015" DAPL == 13.93#
D, .022" DANW == 14.41#
A,, .030" DANW == 15.17#
E,, .040 DANW == 14.52#
B,,, .054 DANW == 14.66#
E,,, .074 DANW == 12.21#
total == 113.24#

len 26.5"
E .009" DAPL == 14.18#
len 27"
B, .012" DAPL == 14.69#
len 27.5"
G, .015" DAPL == 15.0#
len 28"
D, .022" DANW == 16.08#
len 28.5"
A,, .030" DANW == 17.55#
len 29"
E,, .040 DANW == 17.39#
len 29.5"
B,,, .054 DANW == 18.16#
len 30"
E,,, .074 DANW == 15.65#
total == 128.72#
"""


class MyTestCase(unittest.TestCase):
    def test_low_scale_after_high(self):
        self.assertRaises(InvalidScaleLengthError, GuitarString, '30-26.5', 'DAPL', .009, 'E', 4)

    def test_bad_input(self):
        self.assertRaises(InvalidScaleLengthError, GuitarString, 'bad_scale_length', 'DAPL', .009, 'E', 4)
        self.assertRaises(OutOfRangeError, GuitarString, 0, 'DAPL', .009, 'E', 4)

        self.assertRaises(InvalidNoteError, GuitarString, 26.5, 'DAPL', .009, 'cherry', 4)
        self.assertRaises(InvalidNoteError, GuitarString, 26.5, 'DAPL', .009, 3, 4)

        self.assertRaises(InvalidStringMaterialError, GuitarString, 26.5, 'XXX', .009, 'E', 4)
        self.assertRaises(InvalidStringMaterialError, GuitarString, 26.5, 0, .009, 'E', 4)

        self.assertRaises(OutOfRangeError, GuitarString, 26.5, 'DAPL', .009, 'E', -1)
        self.assertRaises(OutOfRangeError, GuitarString, 26.5, 'DAPL', .009, 'E', 11)
        self.assertRaises(InvalidOctaveError, GuitarString, 26.5, 'DAPL', .009, 'E', 'xxx')

        self.assertRaises(InvalidGaugeError, GuitarString, 26.5, 'DAPL', 'bad_gauge', 'E', 4)
        self.assertRaises(OutOfRangeError, GuitarString, 26.5, 'DAPL', 0, 'E', 4)

    def test_multiscale_tension(self):
        # 26.5-30 DAPL 0.009 A 1 2 1
        # 26.5-3 DAPL 0.001 C 1 0 1
        calc = GuitarString('26.5-30', 'DAPL', .009, 'A', 1, '2', 1)
        tension = float("{0:.2f}".format(calc.tension))
        print("1 A: " + str(tension))

        calc = GuitarString('30-26.5', 'DAPL', .009, 'A', 1, '2', 1)
        tension = float("{0:.2f}".format(calc.tension))
        print("1 A: " + str(tension))
        # calc = GuitarString('27-28.625', 'DAPL', .009, 'E', 4, 8, 1)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("1 E: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DAPL', .013, 'B', 3, 8, 2)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("2 B: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DAPL', .017, 'G', 3, 8, 3)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("3 G: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DANW', .023, 'D', 3, 8, 4)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("4 D: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DANW', .031, 'A', 2, 8, 5)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("5 A: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DANW', .043, 'E', 2, 8, 6)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("6 E: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DANW', .059, 'B', 1, 8, 7)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("7 B: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DANW', .079, 'E', 1, 8, 8)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("8 E: " + str(tension))


        # calc = GuitarString('27-28.625', 'DAPL', .009, 'E', 4, 8, 1)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("1 E: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DAPL', .012, 'B', 3, 8, 2)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("2 B: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DAPL', .015, 'G', 3, 8, 3)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("3 G: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DAPL', .020, 'D', 3, 8, 4)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("4 D: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DANW', .028, 'A', 2, 8, 5)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("5 A: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DANW', .038, 'E', 2, 8, 6)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("6 E: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DANW', .050, 'B', 1, 8, 7)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("7 B: " + str(tension))
        #
        # calc = GuitarString('27-28.625', 'DANW', .074, 'E', 1, 8, 8)
        # tension = float("{0:.2f}".format(calc.tension))
        # print("8 E: " + str(tension))
        #

        # len 26.5"
        # E .009" DAPL == 14.18#
        # calc = GuitarString(26.5, 'DAPL', .009, 'E', 4)
        # tension = float("{0:.2f}".format(calc.calculate_tension()))
        # calc_m = GuitarString('26.5-30', 'DAPL', .009, 'E', 4, 8, 1)
        # tension_m = float("{0:.2f}".format(calc_m.tension))
        # self.assertEqual(tension_m, tension)
        #
        # #len 27"
        # #B, .012" DAPL == 14.69#
        # calc = GuitarString(27, 'DAPL', .012, 'B', 3)
        # tension = float("{0:.2f}".format(calc.calculate_tension()))
        # calc_m = GuitarString('26.5-30', 'DAPL', .012, 'B', 3, 8, 2)
        # tension_m = float("{0:.2f}".format(calc_m.tension))
        # self.assertEqual(tension_m, tension)
        #
        # #len 27.5"
        # #G, .015" DAPL == 15.0#
        # calc = GuitarString(27.5, 'DAPL', .015, 'G', 3)
        # tension = float("{0:.2f}".format(calc.calculate_tension()))
        # calc_m = GuitarString('26.5-30', 'DAPL', .015, 'G', 3, 8, 3)
        # tension_m = float("{0:.2f}".format(calc_m.tension))
        # self.assertEqual(tension_m, tension)
        #
        # #len 28"
        # #D, .022" DANW == 16.08#
        # calc = GuitarString(28, 'DANW', .022, 'D', 3)
        # tension = float("{0:.2f}".format(calc.calculate_tension()))
        # calc_m = GuitarString('26.5-30', 'DANW', .022, 'D', 3, 8, 4)
        # tension_m = float("{0:.2f}".format(calc_m.tension))
        # self.assertEqual(tension_m, tension)
        #
        # #len 28.5"
        # #A,, .030" DANW == 17.55#
        # calc = GuitarString(28.5, 'DANW', .030, 'A', 2)
        # tension = float("{0:.2f}".format(calc.calculate_tension()))
        # calc_m = GuitarString('26.5-30', 'DANW', .030, 'A', 2, 8, 5)
        # tension_m = float("{0:.2f}".format(calc_m.tension))
        # self.assertEqual(tension_m, tension)
        #
        # #len 29"
        # #E,, .040 DANW == 17.39#
        # calc = GuitarString(29, 'DANW', .040, 'E', 2)
        # tension = float("{0:.2f}".format(calc.calculate_tension()))
        # calc_m = GuitarString('26.5-30', 'DANW', .040, 'E', 2, 8, 6)
        # tension_m = float("{0:.2f}".format(calc_m.tension))
        # self.assertEqual(tension_m, tension)
        #
        # #len 29.5"
        # #B,,, .054 DANW == 18.16#
        # calc = GuitarString(29.5, 'DANW', .054, 'B', 1)
        # tension = float("{0:.2f}".format(calc.calculate_tension()))
        # calc_m = GuitarString('26.5-30', 'DANW', .054, 'B', 1, 8, 7)
        # tension_m = float("{0:.2f}".format(calc_m.tension))
        # self.assertEqual(tension_m, tension)
        #
        # #len 30"
        # #E,,, .074 DANW == 15.65#
        # calc = GuitarString(30, 'DANW', .074, 'E', 1)
        # tension = float("{0:.2f}".format(calc.calculate_tension()))
        # calc_m = GuitarString('26.5-30', 'DANW', .074, 'E', 1, 8, 8)
        # tension_m = float("{0:.2f}".format(calc_m.tension))
        # self.assertEqual(tension_m, tension)

    def test_calculate_tension(self):
        """
        tests the tension calculation function; the values are slightly off by about +- .1 from the
        source code we based this on. This seems to be due to the way the frequencies are calculated differently

        """

        # test converting lowercase notes to uppercase
        calc1 = GuitarString(26.5, 'DAPL', .009, 'A#/Bb', 4)
        calc2 = GuitarString(26.5, 'DAPL', .009, 'a#/bb', 4)
        self.assertEqual(calc2.tension, calc1.tension)

        calc = GuitarString(26.5, 'CKPLG', .009, 'E', 4)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(14.24, tension)

        # E .009" DAPL == 14.18#
        calc = GuitarString(26.5, 'DAPL', .009, 'E', 4)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(14.17, tension)
        # B, .012" DAPL == 14.15#
        calc = GuitarString(26.5, 'DAPL', .012, 'B', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(14.14, tension)
        # G, .015" DAPL == 13.93#
        calc = GuitarString(26.5, 'DAPL', .015, 'G', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(13.92, tension)
        # D, .022" DANW == 14.41#
        calc = GuitarString(26.5, 'DANW', .022, 'D', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(14.39, tension)
        # A,, .030" DANW == 15.17#
        calc = GuitarString(26.5, 'DANW', .030, 'A', 2)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(15.16, tension)
        # E,, .040 DANW == 14.52#
        calc = GuitarString(26.5, 'DANW', .040, 'E', 2)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(14.50, tension)
        # B,,, .054 DANW == 14.66#
        calc = GuitarString(26.5, 'DANW', .054, 'B', 1)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(14.64, tension)
        # E,,, .074 DANW == 12.21#
        calc = GuitarString(26.5, 'DANW', .074, 'E', 1)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(12.2, tension)

        calc = GuitarString(25.5, 'DAPL', .012, 'E', 4)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(23.33, tension)

        calc = GuitarString(25.5, 'DAPL', .016, 'B', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(23.28, tension)

        calc = GuitarString(25.5, 'DAPB', .024, 'G', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(30.21, tension)

        calc = GuitarString(25.5, 'DAPB', .032, 'D', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(30.5, tension)

        calc = GuitarString(25.5, 'DAPB', .042, 'A', 2)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(29.91, tension)

        calc = GuitarString(25.5, 'DAPB', .053, 'E', 2)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(26.04, tension)

    def test_convert_to_freq(self):
        """
        tests the freq is calculated properly

        """
        calc = GuitarString(1, 'DAPL', .007, 'C', 0)
        freq = float("{0:.2f}".format(calc.freq))
        self.assertEqual(16.35, freq)

        calc = GuitarString(1, 'DAPL', .007, 'C#/Db', 0)
        freq = float("{0:.2f}".format(calc.freq))
        self.assertEqual(17.32, freq)

        calc = GuitarString(26.5, 'DAPL', .009, 'E', 4)
        freq = float("{0:.1f}".format(calc.freq))
        self.assertEqual(329.6, freq)

    def test_convert_to_unit_weight(self):
        """
        tests the unit_weight is converted properly

        """

        calc = GuitarString(26.5, 'DANW', .074, 'G', 1)
        self.assertEqual(.00098869, calc.unit_weight)

        # G,,  .027" DAPL == 10.38#
        calc = GuitarString(25.5, 'DAPL', .027, 'G', 2)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(10.37, tension)
        # G,,  .060" DAPL == 33.08#
        calc = GuitarString(25.5, 'DAPL', .060, 'G', 2)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(33.05, tension)

        calc = GuitarString(1, 'DAPL', .008, 'C#/Db', 0)
        self.assertEqual(.00001418, calc.unit_weight)

        calc = GuitarString(1, 'DAPL', .007, 'C#/Db', 0)
        self.assertEqual(.00001085, calc.unit_weight)

        # B,  .0165" DAPL == 24.8#
        calc = GuitarString(25.5, 'DAPL', .0165, 'B', 3)
        tension = float("{0:.2f}".format(calc.calculate_tension()))
        self.assertEqual(24.78, tension)


    def test_convert_to_halfsteps(self):
        """
        tests the unit_weight is converted properly

        """
        calc = GuitarString(1, 'DAPL', .008, 'C#/Db', 0)
        self.assertEqual(0, calc.convert_to_halfsteps('A', 4))
        self.assertEqual(2, calc.convert_to_halfsteps('B', 4))
        self.assertEqual(15, calc.convert_to_halfsteps('C', 6))
        self.assertEqual(-10, calc.convert_to_halfsteps('B', 3))

    def test_convert_to_unit_weight(self):
        calc = GuitarString(1, 'DAPL', .008, 'C#/Db', 0)
        wt = calc.convert_to_unit_weight('DAPL', .007)
        self.assertEqual(.00001085, wt)


if __name__ == '__main__':
    unittest.main()
