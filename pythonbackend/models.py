from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

NOTE_CHOICES = (('A', 'A'), ('A#/Bb', 'A#/Bb'), ('B', 'B'), ('C', 'C'), ('C#/Db', 'C#/Db'), ('D', 'D'),
                ('D#/Eb','D#/Eb'), ('E','E'), ('F','F'), ('F#/Gb','F#/Gb'), ('G','G'), ('G#/Ab','G#/Ab'))
OCTAVE_RANGE = 11
STRING_TYPE = (("PL", "Plain"), ("PB", "Phosphorus Bronze"), ("NW", "Nickel Wound"), ("XS", "Stainless Steel"),
               ("HR", "Half-Round"))


class StringSet(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class StringSetForm(ModelForm):
    class Meta:
        model = StringSet
        fields = ['name']
        exclude = ('user',)



class String(models.Model):
    string_set = models.ForeignKey(StringSet)
    string_number = models.IntegerField(max_length=2)
    scale_length = models.CharField(max_length=30)
    note = models.CharField(max_length=5, choices=NOTE_CHOICES)
    octave = models.IntegerField(max_length=2, choices=[(octave, octave) for octave in range(OCTAVE_RANGE)])
    gauge = models.DecimalField(max_digits=5, decimal_places=5)
    string_type = models.CharField(max_length=30, choices=STRING_TYPE)

    class Meta:
        ordering = ['string_number']


class StringForm(ModelForm):
    class Meta:
        model = String
        fields = ['string_set', 'string_number', 'scale_length', 'note', 'octave', 'gauge', 'string_type']
