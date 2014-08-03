from .material_dicts import get_material_dict

class InvalidStringMaterialError(KeyError): pass
class InvalidGaugeError(ValueError): pass
class OutOfRangeError(ValueError): pass

class GuitarString():
    def __init__(self, gauge, string_material):
        self.is_valid_string_material(string_material)
        self.string_material = string_material
        self.gauge = self.sanitize_gauge(gauge)
        self.unit_weight = self.convert_to_unit_weight(self.string_material, self.gauge)

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
        material_dict = get_material_dict(string_material)
        gauge_keys = sorted(material_dict.keys())
        max_gauge_index = gauge_keys.index(max(gauge_keys))

        if gauge > max(gauge_keys):
            low_gauge = gauge_keys[max_gauge_index - 2]
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
            low_gauge = gauge_keys[gauge_index - 1]
            high_gauge = gauge_keys[gauge_index]

        low_unit_weight = material_dict[low_gauge]
        high_unit_weight = material_dict[high_gauge]

        unit_weight = low_unit_weight + ((high_unit_weight - low_unit_weight) * (gauge - low_gauge)
                                         / (high_gauge - low_gauge))
        return unit_weight

    @staticmethod
    def is_valid_string_material(string_material):
        """
        converts parameter to an int and raises an appropriate error on failure
        @param string_material:
        @return: @raise InvalidStringMaterialError:
        """
        if get_material_dict(string_material) == 'Invalid':
            raise InvalidStringMaterialError('string_material does not match predefined string materials')
        return True

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