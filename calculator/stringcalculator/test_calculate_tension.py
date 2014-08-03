import unittest
from calculator.stringcalculator.string_calculator import calculate_tension
from calculator.stringcalculator.scientificpitch.scientific_pitch import ScientificPitch
from calculator.stringcalculator.string.length import Length
from calculator.stringcalculator.string.guitar_string import GuitarString
# E   .012" DAPL == 23.35#


class TestGuitarString(unittest.TestCase):
    """test calculate_tension"""

    def test_not_a_number_gauge_input(self):
        pitch = ScientificPitch('e', 4)
        length = Length(25.5)
        string = GuitarString(.012, 'DAPL')
        tension = float("{0:.2f}".format(calculate_tension(length.scale_length, pitch.frequency, string.unit_weight)))
        self.assertEqual(23.33, tension)
