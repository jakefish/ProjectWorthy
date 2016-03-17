from django.db import models
from datetime import datetime


MOVEMENT_LIST = []



class Wod(object):
    String warm_up = ""
    String metcon = ""
    String weightlifting = ""  #foreign key to Weightlifting
    String strength_accessory = ""
    int date = 0

    def __unicode__(self):
       return str(self.date)

    def get_current_page_wod(self):
        """Returns the current workout in any given session """
        for wod in self.wods:
            if wod == current:
                return current_wod
        return current_wod

class WeightLifting(object):

    String movement= "" #foreign key to movement
    String weightlifting_name = ""
    int number_of_movements = 0
    int rank = 0

    def __unicode__(self):
       return str(self.weightlifting_name)

class Movement(object):
    String type = ['Cardio', 'Strength', 'Gymnastic']
    movement_list = []
    String movement_name = ""


    def __unicode__(self):
          return str(self.movement_name)
