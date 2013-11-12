__author__ = 'mattlodes'
from django import forms

ACCEPTED_NOTES = ["A", "Ab", "B#", "B", "C", "D", "E", "F", "G"]
OCATAVE_RANGE = 11


class StringForm(forms.Form):
    Octave = forms.ChoiceField(choices=[(x, x) for x in range(OCATAVE_RANGE)])
    String_Type = forms.CharField()
    Metric = forms.BooleanField(required=False)
    Note = forms.ChoiceField(choices=[(index, index) for index in ACCEPTED_NOTES])
    Gauge = forms.DecimalField()
