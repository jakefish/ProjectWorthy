import datetime

from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.core import management

from wod.models import Wod, WeightLifting, Athlete


@override_settings(
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )
)
class TestModels(TestCase):

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

    def test_load_data_call_command(self):
        management.call_command('load_data')
        self.assertTrue(Wod.objects.all().count(), 200)
        Wod.objects.all().delete()
        self.assertTrue(Wod.objects.all().count() == 0)
        self.assertTrue(WeightLifting.objects.all().count(), 200)
        WeightLifting.objects.all().delete()
        self.assertTrue(WeightLifting.objects.all().count() == 0)
