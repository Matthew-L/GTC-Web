__author__ = 'mattlodes'
from django import forms



ACCEPTED_NOTES = ['A', 'C', 'C#/Db', 'D', 'Eb/D#', 'E', 'F', 'F#/Gb', 'G', 'Ab/G#']
OCTAVE_RANGE = 11
STRING_TYPE = [("PL","Plain"), ("PB","Phosphorus Bronze"), ("NW","Nickel Wound"), ("XS", "Stainless Steel"), ("HR","Half-Round")]

class StringForm(forms.Form):
    Scale_Length = forms.FloatField()
    Octave = forms.ChoiceField(choices=[(octave, octave) for octave in range(OCTAVE_RANGE)])
    String_Type = forms.ChoiceField(choices=STRING_TYPE)
    Note = forms.ChoiceField(choices=[(index, index) for index in ACCEPTED_NOTES])
    Gauge = forms.FloatField()
