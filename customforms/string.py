__author__ = 'mattlodes'
from django import forms
#from django.forms import ModelForm
#from pythonbackend.models import strings


ACCEPTED_NOTES = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']
OCTAVE_RANGE = 11
STRING_TYPE = [("PL","Plain"), ("PB","Phosphorus Bronze"), ("NW","Nickel Wound"), ("XS", "Stainless Steel"), ("HR","Half-Round")]

class StringForm(forms.Form):
    Scale_Length = forms.FloatField()
    Note = forms.ChoiceField(choices=[(index, index) for index in ACCEPTED_NOTES])
    Octave = forms.ChoiceField(choices=[(octave, octave) for octave in range(OCTAVE_RANGE)])
    Gauge = forms.FloatField()
    String_Type = forms.ChoiceField(choices=STRING_TYPE)


class SubmitStringForm(forms.Form):
    Username = forms.CharField(widget=forms.HiddenInput())
    Scale_Length = forms.FloatField(widget=forms.HiddenInput())
    Note = forms.CharField(widget=forms.HiddenInput())
    Octave = forms.IntegerField(widget=forms.HiddenInput())
    Gauge = forms.FloatField(widget=forms.HiddenInput())
    String_Type = forms.CharField(widget=forms.HiddenInput())

