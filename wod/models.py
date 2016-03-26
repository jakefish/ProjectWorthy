from django.db import models
from datetime import datetime

from django.contrib.auth.models import User


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

class Athlete(models.Model):

    workouts_completed = models.IntegerField(default=0)
    personal_records = models.IntegerField(default=0)
    favorite_movement = models.OneToOneField('WeightLifting')
    athlete = models.ForeignKey(User)

    def __unicode__(self):
       return str(self.athlete)
