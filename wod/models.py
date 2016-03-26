from django.db import models
from datetime import datetime



class Wod(models.Model):
    warm_up = models.TextField()
    metcon = models.TextField()
    weightlifting = models.ManyToManyField('WeightLifting')
    strength_accessory = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)

    def __unicode__(self):
       return str(self.date)


class WeightLifting(models.Model):
    movement = models.CharField(max_length=50)
    rep_scheme = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)

    def __unicode__(self):
       return str(self.movement)
