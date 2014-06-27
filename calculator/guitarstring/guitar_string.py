from calculator.guitarstring import material_dicts

class InvalidScaleLengthError(ValueError): pass
class InvalidNoteError(KeyError): pass
class InvalidStringMaterialError(KeyError): pass
class InvalidOctaveError(ValueError): pass
class InvalidGaugeError(ValueError): pass
class OutOfRangeError(ValueError): pass
class InvalidStringNumberError(ValueError): pass


class GuitarString():
    """
    GuitarString is a class used to calculate the tension of a given string
    using the parameters: scale_length, string_material, gauge, note, octave.
    These parameters are defined in the constructor.
    """
    number_of_strings = 0
    string_number = 0
    scale_length = 0
    unit_weight = 0
    freq = 0
    tension = 0
    string_material = 'Unknown'
    octave = 0
    note = 'Unknown'
    gauge = 0
    tension_constant = 386.4
    note_dict = {'C':       0,
                 'C#/Db':   1,
                 'D':       2,
                 'D#/Eb':   3,
                 'E':       4,
                 'F':       5,
                 'F#/Gb':   6,
                 'G':       7,
                 'G#/Ab':   8,
                 'A':       9,
                 'A#/Bb':   10,
                 'B':       11}

    def __init__(self, scale_length, string_material, gauge, note, octave, number_of_strings=None, string_number=None):
        """
        Needs to be rewritten...
        Constructor for calculator class;
        initializes scale_length,
        frequency: using note and octave,
        and unit_weight: using string_material and gauge

        @param scale_length: the length of the guitar; used for string tension calculations
        @param string_material: the material the string is made of;
                                5 types due to the limited data provided by string manufacturers
                                used to calculate unit_weight
        @param gauge: the diameter of the string that is having its tension calculated
                        used to calculate the unit_weight
        @param note: the note the string is tuned to, one of the 12 notes possible; used to calculate the frequency
        @param octave: the octave of the note the string is being tuned to; used to calculate unit_weight
        """

        print(scale_length, string_material, gauge, note, octave, number_of_strings, string_number)

        self.is_valid_string_material(string_material)
        self.string_material = string_material
        self.gauge = self.sanitize_gauge(gauge)
        self.note = self.sanitize_note(note)
        self.octave = self.sanitize_octave(octave)

        if str(scale_length).find('-') != -1:
            if number_of_strings is None or string_number is None:
                raise InvalidScaleLengthError("Multi-scale scale_lengths (scale_lengths containing \'-\'"
                                              " must specify the number of strings and string_number")
            self.number_of_strings = self.sanitize_number_of_strings(number_of_strings)
            self.string_number = self.sanitize_string_number(string_number)
            if self.string_number > self.number_of_strings:
                raise OutOfRangeError(' string_number must be less than number_of_strings')

            self.scale_length = self.convert_multiscale_to_scale_length(scale_length, self.number_of_strings, self.string_number)
        else:
            self.scale_length = self.sanitize_scale_length(scale_length)

        self.freq = self.convert_to_freq(self.note, self.octave)
        self.unit_weight = self.convert_to_unit_weight(self.string_material, self.gauge)

        self.tension = self.calculate_tension()


    def convert_multiscale_to_scale_length(self, scale_length, number_of_strings, string_number):
        """
        Takes the scale_length as a str and transforms it into the scale length range (two separate values)
        By using the total number of strings and the current string's string_number the current strings
        scale_length is calculated.

        @param scale_length: a string containing two floats separated by a hyphen
        @param number_of_strings: the total numbers of strings the multi-scale neck spans
        @param string_number: the current strings number (the higher the string typically the lower the number)
                                high e on standard would be a 1
                                low E on standard would be a 6
        @return: the current strings scale_length
        """
        high_scale_length, low_scale_length = self.sanitize_multiscale(scale_length)

        if high_scale_length < low_scale_length:
            #InvalidScaleLengthError('Multi-scale scale_lengths must follow a format similar to \'26.5-30\' and the lower value comes first')
            temp = high_scale_length
            high_scale_length = low_scale_length
            low_scale_length = temp

        fan_distance = high_scale_length - low_scale_length
        if number_of_strings > 1:
            scale_constant = fan_distance/(number_of_strings-1)
        else:
            scale_constant = 0

        return low_scale_length + (string_number-1) * scale_constant

    def calculate_tension(self):
        """
        Method of tension calculation provided by D'Addario
        @return: the calculated tension using  (UnitWeight x (2 x ScaleLength x Frequency)^2)/TensionConstant
        """
        tension = (self.unit_weight * (2*self.scale_length*self.freq)**2)/self.tension_constant
        return tension

    def convert_to_halfsteps(self, note, octave):
        """
        Calculates the number of half-steps between any given note and A4
        @param note: the note which is having its half-steps calculated
        @param octave: the octave of the note
        @return: the number of half-steps between A4 and the note-octave combo
        """
        offset = 3
        base_octave = 5  # based off of C5
        octave_offset = (octave - base_octave)*12
        note_offset = self.note_dict[note]
        return offset + octave_offset + note_offset

    def convert_to_freq(self, note, octave):
        """
        Needs to be rewritten...
        uses note and octave to calculate the frequency by using the dictionary of base frequencies
        Follows the equation: Frequency = BaseFrequncy * 2^Octave
        @param note: the note being converted to a frequency
        @param octave: the octave of the note being converted to a frequency
        @return: the frequency of the note and octave
        """
        half_steps = self.convert_to_halfsteps(note, octave)
        A4_freq = 440
        return A4_freq*(2**(1/12))**half_steps
    
    @staticmethod
    def convert_to_unit_weight(string_material, gauge):
        """
        Needs to be rewritten...
        cycles through an array of the appropriate string materials, comparing each entry to the gauge
        if the gauge in the reversed sorted list of keys is less than the given gauge then we have found
        the closest match our hardcoded dictionary values allow for
        @param string_material: one of 5 types used to determine which array to fetch
        @param gauge: the desired gauge, used to find the unit weight in the material_dict
        @return: the closest matched unit_weight to the gauge of the given material
        """
        material_dict = material_dicts.get_material_dict(string_material)
        gauge_keys = sorted(material_dict.keys())
        max_gauge_index = gauge_keys.index(max(gauge_keys))

        if gauge > max(gauge_keys):
            low_gauge = gauge_keys[max_gauge_index-2]
            high_gauge = max(gauge_keys)
        elif gauge < min(gauge_keys):
            low_gauge = gauge_keys[0]
            high_gauge = gauge_keys[2]
        else:
            gauge_index = 0
            for matched_gauge in gauge_keys:
                if gauge < matched_gauge:
                    break
                gauge_index += 1
            low_gauge = gauge_keys[gauge_index-1]
            high_gauge = gauge_keys[gauge_index]

        low_unit_weight = material_dict[low_gauge]
        high_unit_weight = material_dict[high_gauge]

        unit_weight = low_unit_weight + ((high_unit_weight - low_unit_weight) * (gauge - low_gauge)
                                                                            / (high_gauge - low_gauge))
        return unit_weight

    @staticmethod
    def sanitize_string_number(string_number):
        """
        converts both parameters to an int and raises an appropriate error on failure
        @param number_of_strings:
        @param string_number:
        @return: @raise InvalidStringNumberError:
        """
        try:
            string_number = int(float(string_number))
        except ValueError:
            raise InvalidStringNumberError('string_number must be an integer')
        if string_number <= 0:
            raise OutOfRangeError(' string_number must be positive')
        return string_number

    @staticmethod
    def sanitize_number_of_strings(number_of_strings):
        try:
            number_of_strings = int(float(number_of_strings))
        except ValueError:
            raise InvalidStringNumberError('number_of_strings must be an integer')
        if number_of_strings <= 0:
            raise OutOfRangeError('number_of_strings must be positive')
        return number_of_strings

    # @staticmethod
    # def is_valid_string_number_and_number_of_strings(string_number, number_of_strings):
    #     if string_number > number_of_strings:
    #         raise OutOfRangeError(' string_number must be less than number_of_strings')

    @staticmethod
    def is_valid_string_material(string_material):
        """
        converts parameter to an int and raises an appropriate error on failure
        @param string_material:
        @return: @raise InvalidStringMaterialError:
        """
        if material_dicts.get_material_dict(string_material) == 'Invalid':
            raise InvalidStringMaterialError('string_material does not match predefined string materials')
        return True
    @staticmethod
    def sanitize_note( note):
        """
        checks validity of note
        @param note:
        @return: @raise InvalidNoteError:
        """
        note_dict = {'C':       0,
                     'C#/Db':   1,
                     'D':       2,
                     'D#/Eb':   3,
                     'E':       4,
                     'F':       5,
                     'F#/Gb':   6,
                     'G':       7,
                     'G#/Ab':   8,
                     'A':       9,
                     'A#/Bb':   10,
                     'B':       11}
        try:
            if len(note) == 5:
                note = note[0].upper() + '#/' + note[3].upper() + 'b'
            else:
                note = note.upper()
            note_dict[note]
        except (KeyError, TypeError):
            raise InvalidNoteError('note does not match specified format')
        return note
    
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
        if not (0 <= octave <= 9):
            raise OutOfRangeError('octave must be fall between 0 and 9 (inclusive)')

        return octave
    
    @staticmethod
    def sanitize_gauge(gauge):
        """
        converts parameter to an float and raises an appropriate error on failure
        also checks that the scale length is above zero or it will throw OutOfRangeError
        @param gauge:
        @return: @raise OutOfRangeError:
        """
        try:
            gauge = float(gauge)
        except ValueError:
            raise InvalidGaugeError('gauge must be a float')
        if gauge <= 0:
            raise OutOfRangeError('gauge must be a positive number')
        return gauge
    
    @staticmethod
    def sanitize_scale_length(scale_length):
        """
        converts parameter to an float and raises an appropriate error on failure
        also checks that the scale length is above zero or it will throw OutOfRangeError
        @param scale_length:
        @return: @raise OutOfRangeError:
        """
        try:
            scale_length = float(scale_length)
        except ValueError:
            raise InvalidScaleLengthError('scale_length must be a float')
        if scale_length <= 0:
            raise OutOfRangeError('scale_length must be a positive number')
        return scale_length

    @staticmethod
    def sanitize_multiscale( scale_length):
        low_scale_length, high_scale_length= scale_length.split('-')
        try:
            low_scale_length = float(low_scale_length)
            high_scale_length = float(high_scale_length)
        except ValueError:
            raise InvalidScaleLengthError('a multi scale_length must be two floats separated by a \'-\'')
        if high_scale_length <= 0 or low_scale_length <= 0:
            raise OutOfRangeError('both multi scale_lengths must be a positive number')
        return high_scale_length, low_scale_length