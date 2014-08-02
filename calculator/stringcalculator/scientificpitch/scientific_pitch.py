class InvalidNoteError(KeyError): pass
class InvalidOctaveError(ValueError): pass
class OutOfRangeError(ValueError): pass


notes_in_half_steps = {'C': 0,
                       'C#/Db': 1,
                       'D': 2,
                       'D#/Eb': 3,
                       'E': 4,
                       'F': 5,
                       'F#/Gb': 6,
                       'G': 7,
                       'G#/Ab': 8,
                       'A': 9,
                       'A#/Bb': 10,
                       'B': 11}


class ScientificPitch():
    def __init__(self, note, octave):
        self.note = self.sanitize_note(note)
        self.octave = self.sanitize_octave(octave)
        self.frequency = self.convert_to_frequency(self.note, self.octave)

    def convert_to_frequency(self, note, octave):
        """
        Needs to be rewritten...
        uses note and octave to calculate the frequency by using the dictionary of base frequencies
        Follows the equation: Frequency = BaseFrequncy * 2^Octave
        @param note: the note being converted to a frequency
        @param octave: the octave of the note being converted to a frequency
        @return: the frequency of the note and octave
        """
        half_steps = self.convert_to_half_steps(note, octave)
        A4_frequency = 440
        return A4_frequency * (2 ** (1.0 / 12.0)) ** half_steps

    @staticmethod
    def convert_to_half_steps(note, octave):
        """
        Calculates the number of half-steps between any given note and A4
        @param note: the note which is having its half-steps calculated
        @param octave: the octave of the note
        @return: the number of half-steps between A4 and the note-octave combo
        """
        offset = 3
        base_octave = 5  # based off of C5
        octave_offset = (octave - base_octave) * 12
        note_offset = notes_in_half_steps[note]
        return offset + octave_offset + note_offset

    @staticmethod
    def sanitize_octave(octave):
        """
        converts parameter to an int and raises an appropriate error on failure
        @param octave:
        @return: @raise OutOfRangeError:
        """
        try:
            octave = int(octave)
        except ValueError:
            raise InvalidOctaveError('octave must be an integer')
        if not (0 <= octave <= 10):
            raise OutOfRangeError('octave must be fall between 0 and 9 (inclusive)')

        return octave

    @staticmethod
    def sanitize_note(note):
        """
        checks validity of note
        @param note:
        @return: @raise InvalidNoteError:
        """
        try:
            if len(note) == 5:
                note = note[0].upper() + '#/' + note[3].upper() + 'b'
            else:
                note = note.upper()
            notes_in_half_steps[note]
        except (KeyError, TypeError):
            raise InvalidNoteError('note does not match specified format')
        return note