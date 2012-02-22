from django.test import TestCase
from testassignment.t3_httplog.models import HttpRequestLogEntry
from django.test.client import Client


class HRLEPriorityTest(TestCase):
    def test_httprequest_logging(self):

        client = Client()
        response = client.get('/')

        hrle = HttpRequestLogEntry.objects.get(path='/')

        self.assertNotEquals(hrle, None)
        self.assertEquals(hrle.request_method, 'GET')
        self.assertEquals(hrle.priority, 0)