from django.db import models


class strings(models.Model):
    username = models.CharField(max_length=20)
    scale_length = models.DecimalField(decimal_places=4, max_digits=8)
    note = models.CharField(max_length=10)
    octave = models.IntegerField(max_length=2)
    gauge = models.DecimalField(decimal_places=4 ,max_digits=10)
    string_type = models.CharField(max_length=2)

    def __unicode__(self):
        return "username:" + self.username + ", scale_length:" + str(self.scale_length)
