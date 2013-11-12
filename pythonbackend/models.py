from django.db import models


class strings(models.Model):
    username = models.CharField()
    scale_length = models.DecimalField()
    octave = models.IntegerField()
    string_type = models.CharField()
    note = models.CharField()
    gauge = models.DecimalField()