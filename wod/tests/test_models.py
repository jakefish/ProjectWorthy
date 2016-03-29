import datetime

from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse

from wod.models import Wod, WeightLifting, Athlete


@override_settings(
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )
)
class TestModels(TestCase):
    """Test the creation and object database relationships

    This class inherits from django's TestCase sets up and creates a
    temporary test database to run tests.
    """

    def setUp(self):
        """Set up the client."""
        self.c = Client()
        self.user = User.objects.create_user('john', 'js@asp.net', 'password')
        self.user.save()
        self.c.login(username='john', password='password')
        session = self.c.session
        session.save()
        re = 'test'
        Group.objects.get_or_create(name=re)
        grp_obj = Group.objects.get(name=re)
        grp_obj.user_set.add(self.user)

    def test_wod_models(self):
        """Test creation and relationship of Wod objects."""
        weightlifting = WeightLifting()
        weightlifting.movement = 'test'
        weightlifting.rep_scheme = 'test'
        weightlifting.description = 'test'
        weightlifting.save()
        wod = Wod()
        wod_pk = wod.pk
        wod.warm_up = 'warm up'
        wod.metcon = 'metcon'
        wod.strength_accessory = 'strength accessory'
        wod.save()
        wod.weightlifting.add(weightlifting)

        self.assertEqual(wod.pk, 1)
        self.assertEqual(wod.warm_up, 'warm up')
        self.assertEqual(wod.strength_accessory, 'strength accessory')
        self.assertEqual(wod.metcon, 'metcon')
        self.assertFalse(isinstance(wod.weightlifting, WeightLifting))

    def test_weightlifting_model(self):
        """Test creation and relationship of WeightLifting objects."""
        weightlifting = WeightLifting()
        weightlifting_pk = weightlifting.pk
        weightlifting.movement = 'movement'
        weightlifting.rep_scheme = 'rep_scheme'
        weightlifting.description = 'description'
        weightlifting.save()

        self.assertEqual(weightlifting.pk, 1)
        self.assertEqual(weightlifting.movement, 'movement')
        self.assertEqual(weightlifting.rep_scheme, 'rep_scheme')
        self.assertEqual(weightlifting.description, 'description')

    def test_athlete_model(self):
        """Test relationship and creation of Athlete objects. """
        weightlifting = WeightLifting()
        weightlifting_pk = weightlifting.pk
        weightlifting.movement = 'movement'
        weightlifting.rep_scheme = 'rep_scheme'
        weightlifting.description = 'description'
        weightlifting.save()
        weight = WeightLifting.objects.create(movement='movement', rep_scheme='rep_scheme',
                                    description='description')
        athlete = Athlete.objects.create(favorite_movement=weight, athlete=self.user)
        self.assertEqual(athlete.workouts_completed, 0)
        self.assertEqual(athlete.personal_records, 0)
        self.assertEqual(athlete.favorite_movement, weight)
        athlete.workouts_completed = 9
        athlete.personal_records = 101
        self.assertTrue(athlete.workouts_completed == 9)
        self.assertTrue(athlete.personal_records == 101)
