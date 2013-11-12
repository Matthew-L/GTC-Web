__author__ = 'mattlodes'
from django import forms
from pythonbackend.models import strings



ACCEPTED_NOTES = ['A', 'C', 'C#/Db', 'D', 'Eb/D#', 'E', 'F', 'F#/Gb', 'G', 'Ab/G#']
OCTAVE_RANGE = 11
STRING_TYPE = [("PL","Plain"), ("PB","Phosphorus Bronze"), ("NW","Nickel Wound"), ("XS", "XS"), ("HR","Half-Round")]

class StringForm(forms.Form):
    Scale_Length = forms.FloatField()
    Octave = forms.ChoiceField(choices=[(octave, octave) for octave in range(OCTAVE_RANGE)])
    String_Type = forms.ChoiceField(choices=STRING_TYPE)
    Note = forms.ChoiceField(choices=[(index, index) for index in ACCEPTED_NOTES])
    Gauge = forms.FloatField()


class SaveStringSet(forms.Form):
    Scale_Length = forms.FloatField(widget=forms.HiddenInput())
    Octave = forms.IntegerField(widget=forms.HiddenInput())
    String_Type = forms.CharField(widget=forms.HiddenInput())
    Note = forms.CharField(widget=forms.HiddenInput())
    Gauge = forms.FloatField(widget=forms.HiddenInput())





