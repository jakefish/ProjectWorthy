from django.db import models

# Create your models here.
class Wod(models.Model):
    warm_up = models.TextField()
    metcon = models.TextField()
    weightlifting = models.TextField()
    strength_accessory = models.TextField()
