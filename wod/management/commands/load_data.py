import os
import random
import time
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from wod.models import Wod, WeightLifting


class Command(BaseCommand):
    """Command for loading test data.

    Overrides from django's BaseCommand class, this command takes no
    arguments.

    Generates random django objects based off of the weightliftings, movements,
    rep_schemes, descriptoins, warm_ups, and metcon lists which will then be
    used for test data for the wod app.
    """

    def handle(self, *args, **options):

        weightliftings = ['Clean', 'Snatch', 'Deadlift', 'High Hang Snatch',
                            'Hang Snatch', 'Power Clean', 'Back Squat',
                            'Front Squat', 'Clean and Jerk', 'Clean Deadlift',
                            'Clean From Blocks', 'Clean Pull', 'Clean Shrug',
                            'Frankenstein Squat', 'Hang Clean',
                            'Hang Clean - Below the knees',
                            'Hang Snatch - Below the Knees',
                            'Jerk Balance', 'Jerk Dip Squat', 'Muscle Snatch',
                            'Olympic Squat', 'Overhead Squat', 'Overhead Squat',
                            'Power Clean from blocks', 'Power Jerk', 'Power Snatch',
                            'Push Press', 'Rack Delivery', 'Romanian Deadlift',
                            'Snatch Deadlift', 'Snatch Shrug', 'Split Clean',
                            'Split Jerk', 'Split Snatch', 'Tall Muscle Snatch',
                            'Front Squat',
                            ]

        movements = ['Air Squat', 'Back Extensions', 'Box Jump', 'Burpee',
                    'Handstand Push Up', 'Jump Rope', 'Double Unders',
                    'Knees-to-Elbows', 'Lunge', 'Muscle-Up', 'Ring Dip',
                    'Pull-Up', 'Push-Up', 'Dips', 'Sit-Up', 'Rope Climb',
                    'Kettlebell Swing', 'Press', 'Thruster', 'Tire Flip',
                    'Prowler', 'Wall Ball', 'Running', 'Rowing']

        rep_schemes = ['5X5', '3X3', 'EMOM', 'E2M', '21-15-9', '5/3/1', '10/5/5/5/10',
                        '9/6/3/6/9', '3/6/9/12/15/', 'Max reps ', '1RM','3RM', '5RM',
                        '10RM', '15RM','30RM', '50RM','AHAP', 'AFAP','FOR TIME',
                         'TABATA','MAX ROUNDS IN 20 MINUTES', '3 ROUNDS','10 ROUNDS'
                         'CHIPPER', 'COUPLET', 'DEATH-BY','ENDURANCE', 'GIRLS', 'GRID',
                         'HERO', 'HYBRID', 'Kettlebell','LADDER', 'KIDS','ROWING', 'SINGLET',
                         'STRENGTH BIAS','STRONGMAN', 'SWIMMING', 'TABATA','TIME CAP',
                         'TRIPLET']

        descriptions = [
                        'Push hard', 'Do not give up', 'Burner',
                        'Lets see some PRs',
                        'Push yourself','This is a sprint',
                        'Remeber to pull through',
                        'Keep your weight in your heels',
                        'Do not sacrifice form',
                        'This one sucks', 'Keep arms locked out',
                        'Remember to keep your core tight',
                        'Elbows up!', 'Practice',
                        'Warm up properly for this'
                        ]

        warm_ups = [
                    'box jumps', '500m Row', '500m Run', 'Push Ups',
                    'Goblet Squats', 'Good mornings', '5min Assault Bike',
                    'Burpees', 'Hollow Rock', 'Mountain Climber',
                    'Crossover symmetry activation', 'Lunge', 'KB-swing',
                    'Squat', 'Jumping Squat', 'Sots Press',
                    'Snatch Press W/ PVC','Tag', 'Stick Game',
                    'Kip Practice - 3m', 'Walk Walks','Drom', 'Bear Crawls'
                    ]

        metcons = [
                    'Michael', 'Kelly', 'Fran', 'Karen', 'Cindy', 'Elizabeth',
                    'Dianne', 'Nancy', 'Annie', 'Chasing Annie', 'Sally',
                    'Filthy Fifty', 'Amanda', 'Angie', 'Barabara', 'Chelsea',
                    'Crhistine', 'Eva', 'Grace', 'Helen', 'Isabel', 'Jackie',
                    'Linda', 'Lynne', 'Mary', 'Nancy', 'Nicole', 'JT', 'Murph',
                    'Daniel', 'Josh', 'Jason', 'Badger', 'Nate', 'Randy',
                    'Tommy V', 'Ryan', 'Erin', 'Mr. Joshua', 'DT', 'Danny',
                    'Hansen', 'Tyler', 'Stephen', 'Garrett', 'War Frank',
                    'McGhee', 'Paul', 'Jerry', 'Nutts', 'Arnie', 'The Seven',
                    'RJ', 'Luce', 'Roy', 'ADAM BROWN', 'Coe', 'Severin', 'Jack',
                    'Forrest', 'Blake', 'Collin', 'Thompson', 'Whitten', 'Bull',
                    'Rankel', 'Holbrook', 'Ledesma', 'Wittman', 'McCluskey',
                    'Weaver', 'Abbate', 'Hammer', 'Moore', 'Wilmot', 'Moon',
                    'Morrison', 'Small', 'Gator', 'Bradley', 'Meadows',
                    'Santiago', 'Carse', 'Bradshaw','White', 'Santora', 'Wood',
                    'Hidalgo', 'Ricky', 'Dae Han', 'Desforges', 'Rahoi', 'Del',
                    'Pheezy','Jag 28', 'Brian', 'Nick', 'Lumberjack 20',
                    'Brenton', 'Tumilson', 'Ship', 'Jared', 'Tully',
                    'Holleyman','Adrain', 'Glen', 'Tom', 'Moose'
                  ]

        strength_accessories = [
                                'Kick Ups w/ hold', 'Wall Walk', 'HSW',
                                'Parallete Kick Ups w/ hold',
                                '*Arch/Hollow Swings (Kip); 3x20',
                                '*Tabata L-Sit from Paralletes',
                                'MOBILIZE YO-SELF!',
                                'Crossover Symmetry Iron Scap',
                                '*Arch/Hollow Swings (Kip); 3x20',
                                '*HandStand Walk attempt; 3 x',
                                '*Swing: 8-8-8-8-8 EMOTM (124/88#)',
                                '*MU Transitions: 10',
                                '*Arch/Hollow Swings (Kip on Rings); 3x20',
                                '9-9-9-9-9 @124/88#',
                                '10 Band Pull Aparts',
                                '10 Swimmers',
                                '200m Farmer Walk - AHAP',
                                'Supine Ring Rows',
                                '10 Strict Muscle Snatch (empty bar)',
                                '10 Banded Face Pulls',
                                'If interested in OLY work, ask.',
                                'Sled Drag [Backwards] @ 90/45#',
                                'Butcher LoPush: 20m (# 90/# 70)',
                                'Sled push @ 135/95#',
                                '*10 Rds: of Cindy',
                                '400m Farmer Carry',
                                '20 Reverse Hyper',
                                '20 GHD sit up',
                                'Z1 Row or Airdyne',
                                'Pistols 31X1 to box at just below knee height',
                                'Leg Less Rope Climb',
                              ]

        for x in range (0, 200):
            WeightLifting.objects.create(movement=movements[random.randrange(
                                        len(movements))],
                                        rep_scheme=rep_schemes[random.randrange(
                                        len(rep_schemes))],
                                        description=descriptions[random.randrange(
                                        len(descriptions))],
                                        )


        for x in range(0, 200):
            wod = Wod(warm_up=warm_ups[random.randrange(len(
                        warm_ups))],
                        metcon=metcons[random.randrange(len(metcons))],
                        strength_accessory=strength_accessories[random.randrange(
                        len(strength_accessories))]
                        )
            wod.save()
            wod.weightlifting.add(WeightLifting.objects.all()[random.randrange(
            len(weightliftings))])
            wod.weightlifting.add(WeightLifting.objects.all()[random.randrange(
            len(weightliftings))])
