from django.db import models
from datetime import datetime

class Wod(models.Model):
    warm_up = models.TextField()
    metcon = models.TextField()
    weightlifting = models.TextField()
    strength_accessory = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)

    def __unicode__(self):
       return str(self.date)
