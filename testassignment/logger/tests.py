from django.test import TestCase
from models import HttpRequestLogEntry, AuditLogEntry
from django.test.client import Client
from django.core.urlresolvers import reverse
from testassignment.person.models import Contact


class MiddlewareTest(TestCase):
    def test_httprequest_logging(self):
        client = Client()
        response = client.get('/')

        log_entry = HttpRequestLogEntry.objects.get(path='/')
        self.assertNotEquals(log_entry, None)
        self.assertEquals(log_entry.request_method, 'GET')
        self.assertEquals(log_entry.priority, 0)


class AuditLoggerTest(TestCase):
    def setUp(self):
        self._contact = { #copied from fixture
            "bio": "Application Developer, System Administrator \r\nand Researcher in a wide variety of \r\napplications and tools",
            "first_name": "Andrei",
            "last_name": "Pak",
            "dob": "1981-03-13",
            "other_contacts": "http://google.com/profiles/pak.andrei - Google Profile\r\nhttp://pakan.ru - Personal Page",
            "skype": "pak.andrei",
            "jabber": "pak.andrei@gmail.com",
            "email": "pak.andrei@gmail.com",
            #"photo": None
        }


    def test_object_create(self):
        count_before = AuditLogEntry.objects.count()
        contact = Contact.objects.create(**self._contact)
        count_after = AuditLogEntry.objects.count()
        self.assertEqual(count_after - 1, count_before)

        log_entry = AuditLogEntry.objects.latest('date')
        self.assertNotEquals(log_entry, None)
        self.assertEquals(log_entry.model, contact._meta.object_name)
        self.assertEquals(log_entry.instance, unicode(contact))
        self.assertEquals(log_entry.action, AuditLogEntry.ACTION_CREATE)

    def test_object_update(self):

        count_before = AuditLogEntry.objects.count()

        contact = Contact.objects.get()
        contact.name = 'Andrey'
        contact.save()

        count_after = AuditLogEntry.objects.count()
        self.assertEqual(count_after - 1, count_before)

        log_entry = AuditLogEntry.objects.latest('date')
        self.assertNotEquals(log_entry, None)
        self.assertEquals(log_entry.model, contact._meta.object_name)
        self.assertEquals(log_entry.instance, unicode(contact))
        self.assertEquals(log_entry.action, AuditLogEntry.ACTION_UPDATE)

    def test_object_delete(self):

        count_before = AuditLogEntry.objects.count()

        contact = Contact.objects.get()
        contact.delete()

        count_after = AuditLogEntry.objects.count()
        self.assertEqual(count_after - 1, count_before)

        log_entry = AuditLogEntry.objects.latest('date')
        self.assertNotEquals(log_entry, None)
        self.assertEquals(log_entry.model, contact._meta.object_name)
        self.assertEquals(log_entry.instance, unicode(contact))
        self.assertEquals(log_entry.action, AuditLogEntry.ACTION_DELETE)
