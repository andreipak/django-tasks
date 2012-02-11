from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from datetime import date
from time import strptime

from testassignment.t1_contact.models import Contact
from django.utils import simplejson as json

VEIW_NAME = 'editmodel'
JSON_MIME = 'application/json' #http://stackoverflow.com/questions/477816/the-right-json-content-type

class AjaxEditFormTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.admin = Client()
        self.admin.login(username='admin', password='admin')

        self._contact = { #copied from fixture
            "bio": "Application Developer, System Administrator \r\nand Researcher in a wide variety of \r\napplications and tools",
            "name": "Andrei",
            #"contacts": "Kharkov, Lugovaya st. 30A/2",
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


    def test_ajax_post(self):
        """
        Check if ajax form post works.
        Good response should look like:

        [{"pk": 1, "model": "t1_contact.contact", "fields":
          {
            "bio": "Application Developer ...",
            ...
            "email": "pak.andrei@gmail.com"
          }
        }]
        """

        response = self.admin.post(
                    reverse(VEIW_NAME),
                    self._contact,
                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')


        self.assertEquals(JSON_MIME in response.get('Content-Type',''), True)

        ro = json.loads(response.content)
        self.assertEquals(isinstance(ro, list), True) #should be list on success
        self.assertEquals(len(ro), 1)
        self.assertEquals(ro[0].get('pk'), 1)
        contact = ro[0]['fields']

        for k in self._contact.keys():
            self.assertEquals(unicode(self._contact[k]), contact.get(k))



    def test_form_validation(self):
        """
        Check if ajax form validation works.
        Server should respond with json:

         {"lastname": ["This field is required."], ...}

        """

        bad_contact  = self._contact.copy()
        bad_contact['name'] = ''
        bad_contact['email'] = 'email'
        bad_contact['dateofbirth'] = '1981'

        response = self.admin.post(
                    reverse(VEIW_NAME),
                    bad_contact,
                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(JSON_MIME in response.get('Content-Type',''), True)

        ro = json.loads(response.content)

        self.assertEquals(isinstance(ro, dict), True)
        self.assertEquals(len(ro.keys()), 3)


        self.assertEquals(ro['name'], ['This field is required.'])
        self.assertEquals(ro['email'], ['Enter a valid e-mail address.'])
        self.assertEquals(ro['dateofbirth'], ['Enter a valid date.'])
