from django.db import models
from django.contrib.auth.models import User


class StringSet(models.Model):
    name = models.CharField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class String(models.Model):
    string_set = models.ForeignKey(StringSet)
    string_number = models.IntegerField()
    scale_length = models.CharField(max_length=30)
    note = models.CharField()
    octave = models.IntegerField()
    gauge = models.DecimalField()
    string_type = models.CharField()

