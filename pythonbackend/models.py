from django.db import models
from django.contrib.auth.models import User


class StringSet(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class String(models.Model):
    string_set = models.ForeignKey(StringSet)
    string_number = models.IntegerField(max_length=2)
    scale_length = models.CharField(max_length=30)
    note = models.CharField(max_length=5)
    octave = models.IntegerField(max_length=2)
    gauge = models.DecimalField(max_digits=5, decimal_places=5)
    string_type = models.CharField(max_length=30)

