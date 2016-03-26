from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Wod(models.Model):
    """Models crossfit workouts.

    Wod stands for Workout of the Day, and is part of the crossfit vernacular.
    Stores common attributes found among typical crossfit workouts.

    Attributes:
        warm_up:              A text field that holds a user defined workout for
                              any given wod.

        metcon:               A text field used to store the main workout and
                              workout name.

        weightlifting:        Has a many to many relationship with weightlifting
                              objects stores the weightlifting movement used in
                              the strength porition of a workout.

        strength_accessory:   A text field used to store and record post workout
                              strength accessories.

        date:                 A date field that tracks when a particular workout
                              was originally created.
    """
    warm_up = models.TextField()
    metcon = models.TextField()
    weightlifting = models.ManyToManyField('WeightLifting')
    strength_accessory = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)

    def __unicode__(self):
        """Returns and displays the string date of a Wod object."""
        return str(self.date)


class WeightLifting(models.Model):
    """Models crossfit weightlifting movements.


    This class stores and models all of the crossfit olypmic and weight lifts.
    This class is of extreme importance as serves as a many to many field in wod
    objects.

    Attributes:
        movement:           A char field that stores the name of a particular
                            movement.

        rep_scheme:         A char field that stores how a movement should be
                            performed.

        description:        A text field for users to make additional comments.

        date:               A date field used to track when a movement is
                            first created.
    """
    movement = models.CharField(max_length=50)
    rep_scheme = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)

    def __unicode__(self):
        """Returns and displays the string date of a WeightLifting object."""
        return str(self.movement)

class Athlete(models.Model):
    """Links users to an athlete to store crossfit specific data.

    This class is used to link a user to an athlete so an athlete can customized.
    their profiles and look at their workout history and performance.

    Attributes:
        workouts_completed:       An integer field that tracks an athletes total
                                  number of workouts completed.

        personal_records:         A integer field that tracks the total number
                                  of personal records an athlete has achieved.

        favorite_movement:        A field that has a one to one relationship
                                  with weightlifting to store an athletes
                                  current favorite movement.

        athlete:                  A foreignkey that represents an athletes
                                  relationship to a site user.
    """
    workouts_completed = models.IntegerField(default=0)
    personal_records = models.IntegerField(default=0)
    favorite_movement = models.OneToOneField('WeightLifting')
    athlete = models.ForeignKey(User)

    def __unicode__(self):
        """Returns and displays the string date of an Athlete object."""
        return str(self.athlete)
