__author__ = 'mattlodes'
from django import forms


class StringForm(forms.Form):
    Octave = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)])
    String_Type = forms.CharField()
    Metric = forms.BooleanField(required=False)
    Note = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])