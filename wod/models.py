from django.db import models

class Wod(models.Model):
    warm_up = models.TextField()
    metcon = models.TextField()
    weightlifting = models.TextField()
    strength_accessory = models.TextField()
    date = models.DateField()

    def __unicode__(self):
       return str(self.date)
