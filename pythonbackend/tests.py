"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from pythonbackend.views import is_valid_result

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_scale_length(self):
        self.assertFalse(is_valid_result(("1w1", "PL", 1, "A", 2)))
        self.assertFalse(is_valid_result(("w", "PL", 1, "A", 2)))
        self.assertFalse(is_valid_result(("-1", "PL", 1, "A", 2)))

        self.assertTrue(is_valid_result(("2", "PL", 1, "A", 2)))

    def test_gauge_length(self):
        self.assertFalse(is_valid_result((1, "PL", "1w1", "A", 2)))
        self.assertFalse(is_valid_result((1, "PL", "w", "A", 2)))
        self.assertFalse(is_valid_result((1, "PL", -1, "A", 2)))

        self.assertTrue(is_valid_result((1, "PL", 1, "A", 2)))



