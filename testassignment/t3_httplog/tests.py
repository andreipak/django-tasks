from django.test import TestCase
from django.contrib.auth.models import User
from models import HttpRequestLogEntry

from django.test.client import Client
from testassignment import views
from django.core.urlresolvers import reverse


class MiddlewareTest(TestCase):
    def test_httprequest_logging(self):

        client = Client()
        url = reverse(views.index)
        response = client.get(url)

        hrle = HttpRequestLogEntry.objects.get(path='/')

        self.assertNotEquals(hrle, None)
        self.assertEquals(hrle.request_method, 'GET')