from random import random, randint

from wod.models import Wod



WEIGHTLIFTING_CHOICES =['Snatch','Clean and Jerk','Deadlift','Backsquat',
'Frontsquat', 'Push Press', 'Sholder Press', 'Split Jerk', 'Front-Rack Lunge']

WARM_UP_CHOICES = ['400m Run', '12 goblet squats, 12 burpees', 'Ring-rows','400m Row']

METCONE_CHOICES =['Annie', 'Angie', 'Badger', 'Barbara', 'Candy', 'CrossFit Total','Fran']

for wod in range(10):
    Wod.objects.create(warm_up=WARM_UP_CHOICES[randint(0,len(WARM_UP_CHOICES)-1)], metcon=
    randint(0,len(METCONE_CHOICES)-1), weightlifting=[randint(0,len(WEIGHTLIFTING_CHOICES)-1)],
        )
