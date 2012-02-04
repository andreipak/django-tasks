from django.test import TestCase
from django.contrib.auth.models import User
from t1_contact.models import Contact

from django.test.client import Client
from testassignment import views
from django.core.urlresolvers import reverse



class InitialDataTest(TestCase):
    def test_adminuser(self):
        """
        check if initial superuser exists and has default credentials
        """

        default_creds = 'admin:admin'
        username, password = default_creds.split(':')

        u = User.objects.get(pk=1)
        self.assertEqual(u.is_superuser, True)
        self.assertEqual(u.username == username, True)
        self.assertEqual(u.check_password(password), True)


    def test_model(self):
        '''
        check if initial contact data exist
        '''
        c = Contact.objects.get(pk=1)
        self.assertEqual(c.pk, 1)

class ModelTest(TestCase):
    def setUp(self):
        self._contact = { #copied from fixture
            "bio": "Application Developer, System Administrator \r\nand Researcher in a wide variety of \r\napplications and tools",
            "name": "Andrei",
            "contacts": "Kharkov, Lugovaya str 30A/2",
            "lastname": "Pak",
            "dateofbirth": "1981-03-13",
            "othercontacts": "http://google.com/profiles/pak.andrei - Google Profile\r\nhttp://pakan.ru - Personal Page",
            "skype": "pak.andrei",
            "jabber": "pak.andrei@gmail.com",
            "email": "pak.andrei@gmail.com"
        }

        self.contact = Contact.objects.create(**self._contact)

    def test_fields(self):
        for k in self._contact.keys():
            self.assertEquals(self._contact[k], getattr(self.contact, k))

    def test_label(self):
        self.assertEquals(
            unicode(self.contact), \
            u'<Contact: %s %s>' % (self._contact['name'], self._contact['lastname'])
        )


class HomeViewTest(TestCase):
    def test_home(self):
        client = Client()
        response = client.get(reverse(views.home))
        self.failUnlessEqual(response.status_code, 200)
