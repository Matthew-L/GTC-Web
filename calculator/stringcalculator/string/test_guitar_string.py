from django.test import TestCase
from calculator.stringcalculator.string.guitar_string import GuitarString, OutOfRangeError, InvalidGaugeError, \
    InvalidStringMaterialError


class TestGuitarString(TestCase):
    """test sanitize_gauge"""

    def test_not_a_number_gauge_input(self):
        self.assertRaises(InvalidGaugeError, GuitarString.sanitize_gauge, 'a')

    def test_negative_gauge_input(self):
        self.assertRaises(OutOfRangeError, GuitarString.sanitize_gauge, 0)

    """test sanitize_string_material"""

    def test_invalid_string_material_input(self):
        self.assertRaises(InvalidStringMaterialError, GuitarString.is_valid_string_material, 'a')

    def test_valid_string_material_input(self):
        self.assertEqual(True, GuitarString.is_valid_string_material('CKPLG'))

    """test GuitarString.init()"""
    def test_valid_gauge_init(self):
        guitar_string = GuitarString(.001, 'CKPLG')
        self.assertEqual(guitar_string.gauge, .001)

    def test_valid_material_init(self):
        guitar_string = GuitarString(.101, 'CKPLG')
        self.assertEqual(guitar_string.string_material, 'CKPLG')

    """test convert_to_unit_weight()"""
    def test_gauge_less_than_min(self):
        self.assertEqual(GuitarString.convert_to_unit_weight(.007, 'CKPLG'), 1.0233999999999999e-05)

    def test_gauge_matches(self):
        self.assertEqual(GuitarString.convert_to_unit_weight(.008, 'CKPLG'), .000014240)

    def test_gauge_greater_than_min(self):
        self.assertEqual(GuitarString.convert_to_unit_weight(.100, 'CKPLG'), 0.0008344310000000007)