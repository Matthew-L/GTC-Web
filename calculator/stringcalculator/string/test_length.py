import unittest
from calculator.stringcalculator.string.length import Length, OutOfRangeError, InvalidScaleLengthError, \
    InvalidStringNumberError


class TestLength(unittest.TestCase):
    """test sanitize_scale_length"""
    def test_not_a_number_scale_length_input(self):
        self.assertRaises(InvalidScaleLengthError, Length.sanitize_scale_length, 'a')

    def test_negative_scale_length_input(self):
        self.assertRaises(OutOfRangeError, Length.sanitize_scale_length, 0)

    def test_valid_scale_length_input(self):
        self.assertEqual(26.5, Length.sanitize_scale_length(26.5))

    def test_valid_int_scale_length_input(self):
        self.assertEqual(24, Length.sanitize_scale_length(24))

    """test sanitize_number"""
    def test_not_a_number_length_number(self):
        self.assertRaises(InvalidStringNumberError, Length.sanitize_number, 'a')

    def test_valid_length_number(self):
        self.assertEqual(6, Length.sanitize_number(6))

    def test_negative_length_number_input(self):
        self.assertRaises(OutOfRangeError, Length.sanitize_number, 0)

    """test sanitize_multiscale"""
    def test_valid_multi_scale_length_input(self):
        high_scale_length, low_scale_length = Length.sanitize_multiscale('27-28.625')
        self.assertEqual(27, low_scale_length)
        self.assertEqual(28.625, high_scale_length)

    def test_not_a_number_multi_scale_length_input(self):
        self.assertRaises(InvalidScaleLengthError, Length.sanitize_multiscale, 'a-z')

    def test_negative_multi_scale_length_input(self):
        self.assertRaises(OutOfRangeError, Length.sanitize_multiscale, '0-12')

    """test Length.scale_length"""
    def test_valid_init_scale_length(self):
        length = Length(25.5)
        self.assertEqual(length.scale_length, 25.5)

    def test_invalid_init_scale_length(self):
        self.assertRaises(InvalidScaleLengthError, Length, 'a')

    """test multiscale Length.scale_length"""
    def test_valid_multiscale_first_string_init_scale_length(self):
        length = Length('25.5-27', 8, 1)
        self.assertEqual(length.scale_length, 25.5)

    def test_valid_multiscale_middle_string_init_scale_length(self):
        length = Length('26.5-30', 8, 5)
        self.assertEqual(length.scale_length, 28.5)

    """test multiscale Length numbers"""
    def test_invalid_number_of_inputs_init(self):
        self.assertRaises(InvalidScaleLengthError, Length, '26.5-30', 1)

    def test_invalid_index_greater_than_total(self):
        self.assertRaises(OutOfRangeError, Length, '26.5-30', 1, 8)

    """test multiscale Length.scale_length"""
    def test_greater_multiscale_length_first(self):
        length = Length('30-26.5', 8, 5)
        self.assertEqual(length.scale_length, 28.5)
