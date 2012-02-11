from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from datetime import date
from time import strptime

from testassignment.t1_contact.models import Contact

VEIW_NAME = 'editform'

class EditFormTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.admin = Client()
        self.admin.login(username='admin', password='admin')

        self._contact = { #copied from fixture
            "bio": "Application Developer, System Administrator \r\nand Researcher in a wide variety of \r\napplications and tools",
            "name": "Andrei",
            "contacts": "Kharkov, Lugovaya st. 30A/2",
            "lastname": "Pak",
            "dateofbirth": "1981-03-13",
            "othercontacts": "http://google.com/profiles/pak.andrei - Google Profile\r\nhttp://pakan.ru - Personal Page",
            "skype": "pak.andrei",
            "jabber": "pak.andrei@gmail.com",
            "email": "pak.andrei@gmail.com",
            #"photo": None
        }


    def test_auth_redirect(self):
        response = self.client.get(reverse(VEIW_NAME))
        self.failUnlessEqual(response.status_code, 302)


    def test_form_post(self):
        response = self.admin.post(reverse(VEIW_NAME), \
                        self._contact, follow=True)

        contact = Contact.objects.get(pk=1)

        for k in self._contact.keys():
            if k == 'dateofbirth':
                 self.assertEquals(
                    date(*strptime(self._contact[k], '%Y-%m-%d')[:3]),
                    contact.dateofbirth
                 )
            else:
                self.assertEquals(unicode(self._contact[k]), getattr(contact, k))

        self.assertRedirects(response, reverse('index'))


    def test_form_validation(self):
        bad_contact  = self._contact.copy()
        bad_contact['name'] = ''
        bad_contact['email'] = 'email'
        bad_contact['dateofbirth'] = '1981'

        response = self.admin.post(
                        reverse(VEIW_NAME),
                        bad_contact, follow=True
                    )


        self.assertContains(response, 'Fix errors below, please')
        self.assertContains(response, 'This field is required')
        self.assertContains(response, 'Enter a valid e-mail address')
        self.assertContains(response, 'Enter a valid date')
