__author__ = 'Micah'

from calculator import material_dicts

class GTC():
    scale_length = 0
    unit_weight = 0
    freq = 0
    tension_constant = 386.4
    freq_dict = {'C':       16.352,
                 'C#/Db':   17.324,
                 'D':       18.354,
                 'Eb/D#':   19.445,
                 'E':       20.602,
                 'F':       21.827,
                 'F#/Gb':   23.125,
                 'G':       24.500,
                 'Ab/G#':   25.957,
                 'A':       27.500,
                 'A#/Bb':   29.135,
                 'B':       30.868}




    def __init__(self, scale_length, string_material, gauge, note, octave):
        self.scale_length = scale_length
        self.freq = self.convert_to_freq(note, octave)
        self.unit_weight = self.convert_to_unit_weight(string_material, gauge)

    #T(Tension) = (UW x (2 x L x F)^2) / 386.4
    def calculate_tension(self):
        tension = (self.unit_weight * (2*self.scale_length*self.freq)**2)/self.tension_constant
        tension = float("{0:.2f}".format(tension))
        return tension

    def convert_to_freq(self, note, octave):
        base_freq = self.freq_dict[note]
        return base_freq * 2**octave

    def convert_to_unit_weight(self, string_material, gauge):
        material_dict = material_dicts.get_material_dict(string_material)

        for g in reversed(sorted(material_dict.keys())):
            if g <= gauge:
                self.unit_weight = material_dict[g]
                return self.unit_weight
