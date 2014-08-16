from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from calculator.views import *
from calculator.stringcalculator.string.length import InvalidScaleLengthError


def decode_json(response):
    return json.loads(response.content.decode('utf8'))


class TestCalculatorViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest',
                       'HTTP_HOST': 'stringulator.com'}

    """test convert_input_to_tenstion"""

    def test_valid_tension_input(self):
        url = reverse('calculator.views.convert_input_to_tension')
        user_input = {'scale_length': '25.5',
                      'total_strings': '',
                      'string_number': '',
                      'note': 'e',
                      'octave': '4',
                      'gauge': '.012',
                      'string_material': 'CKPLG'}

        response = self.client.post(url, user_input, **self.kwargs)
        self.assertEqual(200, response.status_code)
        decoded = decode_json(response)
        self.assertEqual(23.43, decoded['tension'])

    def test_invalid_tension_input(self):
        url = reverse('calculator.views.convert_input_to_tension')
        user_input = {'scale_length': '',
                      'total_strings': '',
                      'string_number': '',
                      'note': 'e',
                      'octave': '4',
                      'gauge': '.012',
                      'string_material': 'CKPLG'}
        response = self.client.post(url, user_input, **self.kwargs)
        self.assertEqual(400, response.status_code)
        decoded = decode_json(response)
        self.assertEqual('There was an error while processing a string.', decoded['error'])

    """ test load_calculate_page """

    def test_load_calculate_without_get_input(self):
        url = reverse('calculator.views.load_calculate_page')
        response = self.client.post(url, {}, **self.kwargs)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'calculate.html')
        self.assertContains(response, '<div id="string-set-name">')
        self.assertRaises(KeyError, lambda: response['string_set_name'])

    # def test_load_calculate_with_valid_get_input(self):
    #     url = reverse('calculator.views.load_calculate_page')
    #     response = self.client.get(url, {'string_set_name': '8 string set', 'users_set': 'micah'}, **self.kwargs)
    #     self.assertEqual(200, response.status_code)
    #     self.assertTemplateUsed(response, 'calculate.html')
    #     self.assertContains(response, '<div id="string-set-name">')
    #
    #     self.assertContains(response, '8 string set')
