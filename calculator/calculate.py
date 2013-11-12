__author__ = 'Micah'

from calculator import material_dicts
class GTC():
    """
    GTC(guitar tension calculator) is a class used to calculate the tension of a given string
    using the parameters: scale_length, string_material, gauge, note, octave.
    These parameters are defined in the constructor.
    """
    scale_length = 0
    unit_weight = 0
    freq = 0
    tension = 0
    string_material = 'Unknown'
    octave = 0
    note = 'Unknown'
    gauge = 0
    tension_constant = 386.4
    freq_dict = {'C': 16.352,
                 'C#/Db': 17.324,
                 'D': 18.354,
                 'Eb/D#': 19.445,
                 'E': 20.602,
                 'F': 21.827,
                 'F#/Gb': 23.125,
                 'G': 24.500,
                 'Ab/G#': 25.957,
                 'A': 27.500,
                 'A#/Bb': 29.135,
                 'B': 30.868}

    def __init__(self, scale_length, string_material, gauge, note, octave):
        """
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
        self.scale_length = scale_length
        self.freq = self.convert_to_freq(note, octave)
        self.unit_weight = self.convert_to_unit_weight(string_material, gauge)
        self.string_material = string_material
        self.octave = octave
        self.note = note
        self.gauge = gauge

    def calculate_tension(self):
        """
        Method of tension calculation provided by D'Addario
        @return: the calculated tension using  (UnitWeight x (2 x ScaleLength x Frequency)^2)/TensionConstant
        """
        tension = (self.unit_weight * (2*self.scale_length*self.freq)**2)/self.tension_constant
        #tension = float("{0:.2f}".format(tension))
        self.tension = tension
        return tension


    def convert_to_halfsteps(self, note, octave):
        offset = 3
        base_octave = 5  # based off of C5
        octave_offset = (octave - base_octave)*12
        note_offset = self.note_dict[note]
        return offset + octave_offset + note_offset
        

      def convert_to_freq(self, note, octave):
        """
        uses note and octave to calculate the frequency by using the dictionary of base frequencies
        Follows the equation: Frequency = BaseFrequncy * 2^Octave
        @param note: the note being converted to a frequency
        @param octave: the octave of the note being converted to a frequency
        @return: the frequency of the note and octave
        """
        half_steps = self.convert_to_halfsteps(note, octave)
        A4_freq = 440
        return A4_freq*(2**(1/12))**half_steps

    def convert_to_unit_weight(self, string_material, gauge):
        """
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

        #for g in reversed(sorted(material_dict.keys())):
        #    if g <= gauge:
        #        self.unit_weight = material_dict[g]
        #        return self.unit_weight
        #if string_material == 'PL':
        #    return 0.221494*gauge**2 + 1.25633*10**-6*gauge-1.24374*10**-8
        #elif string_material == 'PB':
        #    return 0.187794*gauge**2 + 0.00121316*gauge - 0.0000193337
        #elif string_material == 'XS':
        #    return -61.0913*gauge**4 + 10.7501*gauge**3 - 0.482377*gauge**2 + 0.016472*gauge - 0.000135256
        #elif string_material == 'NW':
        #    return -47.8322*gauge**4 + 8.91982*gauge**3 - 0.397346*gauge**2 + 0.0151077*gauge - 0.000126257
        #else:
        #    return 0.179274*gauge**2 + 0.00112123*gauge + 2.18724*10**-6