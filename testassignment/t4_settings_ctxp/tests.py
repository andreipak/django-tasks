from django.test import TestCase
from django.test.client import Client
from testassignment import views
from django.core.urlresolvers import reverse

from django.conf import settings

class SettingsContextProcessorTest(TestCase):
    def test_response(self):
        client = Client()
        response = client.get(reverse(views.index))
        self.assertEquals(response.context['settings'], settings)