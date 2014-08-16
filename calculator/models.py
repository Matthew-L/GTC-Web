from django.db import models
from django.contrib.auth.models import User

NOTE_CHOICES = (('A', 'A'), ('A#/Bb', 'A#/Bb'), ('B', 'B'), ('C', 'C'), ('C#/Db', 'C#/Db'), ('D', 'D'),
                ('D#/Eb', 'D#/Eb'), ('E', 'E'), ('F', 'F'), ('F#/Gb', 'F#/Gb'), ('G', 'G'), ('G#/Ab', 'G#/Ab'))
OCTAVE_RANGE = 10
STRING_TYPE = (("CKPLG", "Plain Steel - CK"),
               ("CKWNG", "Nickel/Steel Hybrid - CK"),
               ("DAPL", "Plain Steel - DA"),
               ("DAPB", "Phosphore Bronze Wound - DA"),
               ("DANW", "Nickel Wound - DA"),
               ("DAXS", "Stainless Steel Wound - DA"),
               ("DAHR", "Half-Round Wound - DA"),
               ("DACG", "Chromes - Stainless Flat wound - DA"),
               ("DAFT", "Flat Tops - Phosphore Bronze  - DA"),
               ("DABW", "80/20 Brass Round Wound - DA"),
               ("DAZW", "85/15 Great American Bronze - DA"),
               ("DAXB", "Bass - Nickel Plated Round Wound - DA"),
               ("DAHB", "Bass - Pure Nickel Half Round - DA"),
               ("DABC", "Bass - Stainless Steel Flat Wound - DA"),
               ("DABS", "Bass - ProSteel Round Wound - DA"))


class StringSet(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    desc = models.CharField(max_length=15000)
    # is_mscale = models.BooleanField()
    number_of_strings = models.IntegerField(max_length=2)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


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
