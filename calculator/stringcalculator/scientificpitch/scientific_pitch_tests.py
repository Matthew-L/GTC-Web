import unittest
from calculator.stringcalculator.scientificpitch.scientific_pitch import ScientificPitch, OutOfRangeError, InvalidNoteError, InvalidOctaveError
# from calculator.guitarstring.guitar_string import GuitarString, InvalidScaleLengthError, OutOfRangeError, \
#     InvalidNoteError, InvalidStringMaterialError, InvalidOctaveError, InvalidGaugeError
class TestScientificPitch(unittest.TestCase):
    def test_out_of_range_octave_input(self):
        self.assertRaises(OutOfRangeError, ScientificPitch.sanitize_octave(-1))

if __name__ == '__main__':
    unittest.main()