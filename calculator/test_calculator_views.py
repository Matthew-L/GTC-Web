from django.test import TestCase, Client
from calculator.views import *


class TestCalculatorViews(TestCase):
    def setUp(self):
        pass

    """test convert_input_to_tenstion"""

    def test_valid_tension_input(self):
        c = Client()
        # Extra parameters to make this a Ajax style request.
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest',
                  'HTTP_HOST': 'stringulator.com'}

        # A valid vote
        # length = Length(tension_input['scale_length'], tension_input['total_strings'], tension_input['string_number'])
        # pitch = ScientificPitch(tension_input['note'], tension_input['octave'])
        # string = GuitarString(tension_input['gauge'], tension_input['string_material'])
        response = c.post('/calculate-tension/', {'scale_length': '25.5',
                                                  'total_strings': '',
                                                  'string_number': '',
                                                  'note': 'e',
                                                  'octave': '4',
                                                  'gauge': '.012',
                                                  'string_material': 'CKWNG'}, **kwargs)
        tension = convert_input_to_tension(response)
        # pitch = ScientificPitch('e', 4)
        # length = Length(25.5)
        # string = GuitarString(.012, 'DAPL')
        # tension = float("{0:.2f}".format(calculate_tension(length, pitch, string)))
        self.assertEqual(23.33, tension)
