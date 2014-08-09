from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from calculator.views import *
from calculator.stringcalculator.string.length import InvalidScaleLengthError

def decode_json(response):
    return json.loads(response.content.decode('utf8'))


class TestCalculatorViews(TestCase):
    def setUp(self):
        pass

    """test convert_input_to_tenstion"""

    def test_valid_tension_input(self):
        client = Client()
        url = reverse('calculator.views.convert_input_to_tension')
        user_input = {'scale_length': '25.5',
                      'total_strings': '',
                      'string_number': '',
                      'note': 'e',
                      'octave': '4',
                      'gauge': '.012',
                      'string_material': 'CKPLG'}
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest',
                  'HTTP_HOST': 'stringulator.com'}
        response = client.post(url, user_input, **kwargs)

        self.assertEqual(200, response.status_code)
        decoded = decode_json(response)
        self.assertEqual(23.43, decoded['tension'])

    def test_invalid_tension_input(self):
        client = Client()

        url = reverse('calculator.views.convert_input_to_tension')
        user_input = {'scale_length': '',
                      'total_strings': '',
                      'string_number': '',
                      'note': 'e',
                      'octave': '4',
                      'gauge': '.012',
                      'string_material': 'CKPLG'}
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest',
                  'HTTP_HOST': 'stringulator.com'}

        self.assertRaises(InvalidScaleLengthError, client.post, url, user_input, **kwargs)