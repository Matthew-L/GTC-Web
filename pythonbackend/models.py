from django.db import models


class strings(models.Model):
    username = models.CharField()
    scale_length = models.DecimalField()
    note = models.CharField()
    octave = models.IntegerField()
    gauge = models.DecimalField()
    string_type = models.CharField()

