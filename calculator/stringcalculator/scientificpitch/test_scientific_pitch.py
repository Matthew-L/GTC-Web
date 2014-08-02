import unittest
from calculator.stringcalculator.scientificpitch.scientific_pitch import ScientificPitch, OutOfRangeError, \
    InvalidNoteError, \
    InvalidOctaveError


class TestScientificPitch(unittest.TestCase):
    """ sanitize_octave()"""

    def test_out_of_range_octave_upper_bound_input(self):
        self.assertRaises(OutOfRangeError, ScientificPitch.sanitize_octave, 11)

    def test_out_of_range_octave_lower_bound_input(self):
        self.assertRaises(OutOfRangeError, ScientificPitch.sanitize_octave, -1)

    def test_invalid_octave_input(self):
        self.assertRaises(ValueError, ScientificPitch.sanitize_octave, 'e')

    def test_valid_octave_input(self):
        for x in range(0, 11):
            self.assertEqual(x, ScientificPitch.sanitize_octave(x))

    """ sanitize_note()"""

    def test_invalid_note_input(self):
        self.assertRaises(InvalidNoteError, ScientificPitch.sanitize_note, 'X')
        self.assertRaises(InvalidNoteError, ScientificPitch.sanitize_note, 1)

    def test_accidental_note_input(self):
        accidentals = ['C#/Db', 'D#/Eb', 'F#/Gb', 'G#/Ab', 'A#/Bb']
        for accidental in accidentals:
            self.assertEqual(accidental, ScientificPitch.sanitize_note(accidental))

    def test_valid_note_input(self):
        notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        for note in notes:
            self.assertEqual(note, ScientificPitch.sanitize_note(note))

    """convert_to_half_steps()"""

    def test_A_n_to_half_steps_input(self):
        note = 'A'
        half_steps_in_octave = 12
        A4_offset = 4
        for n in range(0, 11):
            half_steps = (n - A4_offset) * half_steps_in_octave
            self.assertEqual(half_steps, ScientificPitch.convert_to_half_steps(note, n))

    def test_G_n_to_half_steps_input(self):
        note = 'G'
        G_offset_from_A = 2
        half_steps_in_octave = 12
        A4_offset = 4
        for n in range(0, 11):
            half_steps = (n - A4_offset) * half_steps_in_octave - G_offset_from_A
            self.assertEqual(half_steps, ScientificPitch.convert_to_half_steps(note, n))

    def test_C_n_to_half_steps_input(self):
        note = 'C'
        C_offset_from_A = 9
        half_steps_in_octave = 12
        A4_offset = 4
        for n in range(0, 11):
            half_steps = (n - A4_offset) * half_steps_in_octave - C_offset_from_A
            self.assertEqual(half_steps, ScientificPitch.convert_to_half_steps(note, n))

    """convert_to_frequency()"""
    def test_A4_is_440(self):
        note = 'A'
        octave = 4
        A440 = 440
        pitch = ScientificPitch(note, octave)
        self.assertEqual(A440, pitch.frequency)

    def test_B4_frequency(self):
        note = 'B'
        octave = 4
        B4 = 493.8833012561241
        pitch = ScientificPitch(note, octave)
        self.assertEqual(B4, pitch.frequency)

    def test_C10_frequency(self):
        note = 'C'
        octave = 10
        C10 = 16744.03617923836
        pitch = ScientificPitch(note, octave)
        self.assertEqual(C10, pitch.frequency)