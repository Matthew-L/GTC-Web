from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from south.db import db

NOTE_CHOICES = (('A', 'A'), ('A#/Bb', 'A#/Bb'), ('B', 'B'), ('C', 'C'), ('C#/Db', 'C#/Db'), ('D', 'D'),
                ('D#/Eb','D#/Eb'), ('E','E'), ('F','F'), ('F#/Gb','F#/Gb'), ('G','G'), ('G#/Ab','G#/Ab'))
OCTAVE_RANGE = 11
STRING_TYPE = (("PL", "Plain"), ("PB", "Phosphorus Bronze"), ("NW", "Nickel Wound"), ("XS", "Stainless Steel"),
               ("HR", "Half-Round"))


class StringSet(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    desc = models.CharField(max_length=1000)
    def __unicode__(self):
        return self.name


    class Meta:
        ordering = ['name']


class StringSetForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StringSetForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['hidden'] = True


    class Meta:
        model = StringSet
        fields = ['name', 'user', 'desc']



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
    """
    Generates a form to insert a new user string
    @params user: populates the string_set ChoiceField with the names of the string_sets from that user or
                    if user is None a CharField will appear to make a new name
    """
    def __init__(self, user, *args, **kwargs):
        super(StringForm, self).__init__(*args, **kwargs)
        if user is None:
            self.fields['string_set'] = forms.CharField()
        else:
            string_set_list = []
            for set in StringSet.objects.all():
                if str(set.user) == str(user):
                    string_set_list.append(str(set.name))
            set_tuple = zip(string_set_list, string_set_list)
            set_tuple = tuple(set_tuple)
            self.fields['string_set'] = forms.ChoiceField(set_tuple)

        #self.fields['scale_length'].widget.attrs['hidden'] = True

    class Meta:
        model = String
        #exclude = ['string_set']
