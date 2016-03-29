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

    def test_wod_index_context(self):
        response = self.c.get(reverse('wod_index'), follow=True)
        self.assertTrue(response.status_code == 200)
        self.assertTrue("latest_wod_list" in response.context)
        self.assertTrue("request" in response.context)
        self.assertTrue("user" in response.context)
        self.assertTrue("messages" in response.context)
        self.assertTemplateUsed(response, "wod/wod_archive.html")

    def test_wod_details_context(self):
        response = self.c.get(reverse('wod_index'), follow=True)
        self.assertTrue(response.status_code == 200)
        self.assertTemplateUsed(response, "wod/wod_archive.html")
        management.call_command('load_data')
        response = self.c.get(reverse('wod_index'), follow=True)
        self.assertTrue(len(response.context['latest_wod_list'])!= 0)
        response = self.c.get(reverse('wod_details', kwargs={
                                                            'wod_id': 1,
                                                            }), follow=True)
        self.assertTrue(response.status_code == 200)
        self.assertTemplateUsed(response, "wod/wod_page.html")
        self.assertContains(response, "<p>Wod page</p>")
        self.assertContains(response, "Logout")

    def test_home_context(self):
        self.c.logout()
        response = self.c.get('/home/')
        self.assertTrue(response.status_code == 200)
        self.assertContains(response, 'login')
        self.assertContains(response, 'register')
        print response.content
