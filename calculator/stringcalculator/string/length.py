class InvalidScaleLengthError(ValueError): pass
class OutOfRangeError(ValueError): pass
class InvalidStringNumberError(ValueError): pass


class Length():
    def __init__(self, scale_length, total_strings=None, string_number=None):
        if str(scale_length).find('-') != -1:
            if total_strings is None or string_number is None:
                raise InvalidScaleLengthError("Multi-scale scale_lengths (scale_lengths containing \'-\'"
                                              " must specify the number of strings and string_number")
            self.total_strings = self.sanitize_number(total_strings)
            self.string_number = self.sanitize_number(string_number)
            if self.string_number > self.total_strings:
                raise OutOfRangeError(' string_number must be less than total_strings')

            self.scale_length = self.convert_multiscale_to_scale_length(scale_length, self.total_strings,
                                                                        self.string_number)
        else:
            self.scale_length = self.sanitize_scale_length(scale_length)

    def convert_multiscale_to_scale_length(self, scale_length, total_strings, string_number):
        """
        Takes the scale_length as a str and transforms it into the scale length range (two separate values)
        By using the total number of strings and the current string's string_number the current strings
        scale_length is calculated.

        @param scale_length: a string containing two floats separated by a hyphen
        @param total_strings: the total numbers of strings the multi-scale neck spans
        @param string_number: the current strings number (the higher the string typically the lower the number)
                                high e on standard would be a 1
                                low E on standard would be a 6
        @return: the current strings scale_length
        """
        high_scale_length, low_scale_length = self.sanitize_multiscale(scale_length)

        if high_scale_length < low_scale_length:
            temp = high_scale_length
            high_scale_length = low_scale_length
            low_scale_length = temp

        fan_distance = high_scale_length - low_scale_length
        scale_constant = 0
        if total_strings > 1:
            scale_constant = fan_distance / (total_strings - 1)

        return low_scale_length + (string_number - 1) * scale_constant

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
    def sanitize_multiscale(scale_length):
        try:
            low_scale_length, high_scale_length = scale_length.split('-')
            low_scale_length = float(low_scale_length)
            high_scale_length = float(high_scale_length)
        except ValueError:
            raise InvalidScaleLengthError('a multi scale_length must be two positive floats separated by a \'-\'')
        if high_scale_length <= 0 or low_scale_length <= 0:
            raise OutOfRangeError('both multi scale_lengths must be a strictly positive number')
        return high_scale_length, low_scale_length

    @staticmethod
    def sanitize_number(number):
        """
        converts both parameters to an int and raises an appropriate error on failure
        @param total_strings:
        @param string_number:
        @return: @raise InvalidStringNumberError:
        """
        try:
            number = int(float(number))
        except ValueError:
            raise InvalidStringNumberError('Length numbers must be an integer')
        if number <= 0:
            raise OutOfRangeError('Length numbers must be strictly positive')
        return number
