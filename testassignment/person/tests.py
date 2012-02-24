from django.test import TestCase
from django.contrib.auth.models import User
from models import Contact
from django.conf import settings
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.template import Template, Context
from datetime import date
from time import strptime
from django.core.management import get_commands, call_command

INDEX_VIEW_NAME='index'
EDIT_VIEW_NAME='edit'

CONTACT = { #copied from fixture
    "bio": "Application Developer, System Administrator \r\nand Researcher in a wide variety of \r\napplications and tools",
    "name": "Andrei",
    "contacts": "Kharkov, Lugovaya str 30A/2",
    "lastname": "Pak",
    "dateofbirth": "1981-03-13",
    "othercontacts": "http://google.com/profiles/pak.andrei - Google Profile\r\nhttp://pakan.ru - Personal Page",
    "skype": "pak.andrei",
    "jabber": "pak.andrei@gmail.com",
    "email": "pak.andrei@gmail.com",
    #"photo": None
}


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
        self._contact = CONTACT
        self.contact = Contact.objects.create(**self._contact)

    def test_fields(self):
        for k in self._contact.keys():
            self.assertEquals(self._contact[k], getattr(self.contact, k))

    def test_label(self):
        self.assertEquals(
            unicode(self.contact), \
            u'%s %s' % (self._contact['name'], self._contact['lastname'])
        )


class IndexPageTest(TestCase):
    def test_index(self):
        client = Client()
        response = client.get(reverse(INDEX_VIEW_NAME))
        self.failUnlessEqual(response.status_code, 200)
        self.assertTrue('<!DOCTYPE HTML>' in response.content)


class ModelFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = Client()
        self.admin.login(username='admin', password='admin')
        self._contact = CONTACT

    def test_auth_redirect(self):
        response = self.client.get(reverse(EDIT_VIEW_NAME))
        self.failUnlessEqual(response.status_code, 302)


    def test_form_post(self):
        response = self.admin.post(reverse(EDIT_VIEW_NAME), \
                        self._contact, follow=True)

        self.assertTrue('<!DOCTYPE HTML>' in response.content)

        contact = Contact.objects.get(pk=1)

        for k in self._contact.keys():
            if k == 'dateofbirth':
                 self.assertEquals(
                    date(*strptime(self._contact[k], '%Y-%m-%d')[:3]),
                    contact.dateofbirth
                 )
            else:
                self.assertEquals(unicode(self._contact[k]), getattr(contact, k))

        self.assertRedirects(response, reverse(INDEX_VIEW_NAME))

    def test_form_validation(self):
        bad_contact  = self._contact.copy()
        bad_contact['name'] = ''
        bad_contact['email'] = 'email'
        bad_contact['dateofbirth'] = '1981'

        response = self.admin.post(reverse(EDIT_VIEW_NAME), bad_contact)

        self.assertContains(response, 'This field is required.')
        self.assertContains(response, 'Enter a valid e-mail address.')
        self.assertContains(response, 'Enter a valid date.')



class AjaxFormTest(ModelFormTest):
    """
    AHAH tests
    """

    def setUp(self):
        ModelFormTest.setUp(self)
        self._contact_ajaxForm = self._contact.copy()
        self._contact_ajaxForm['is_ajaxForm'] = '1';


    def test_auth_redirect(self):
        pass


    def test_form_post(self):
        """
        Check if ajaxForm() post works.
        Response should be html rendered by templates/contact_form.html
        """
        response = self.admin.post(reverse(EDIT_VIEW_NAME), self._contact_ajaxForm)


        self.assertFalse('<!DOCTYPE HTML>' in response.content)

        for k in self._contact.keys():
            self.assertContains(response, k)
            self.assertContains(response, self._contact[k])



    def test_form_validation(self):
        """
        Check if validation works while using ajaxForm()

        """

        bad_contact  = self._contact_ajaxForm.copy()
        bad_contact['name'] = ''
        bad_contact['email'] = 'email'
        bad_contact['dateofbirth'] = '1981'

        response = self.admin.post(reverse(EDIT_VIEW_NAME),bad_contact)

        self.assertFalse('<!DOCTYPE HTML>' in response.content)

        self.assertContains(response, 'class="errorField"', count=3)
        self.assertContains(response, 'This field is required.')
        self.assertContains(response, 'Enter a valid e-mail address.')
        self.assertContains(response, 'Enter a valid date.')



class DateWidgetTest(ModelFormTest):
    """
    JQueryUIDatePickerWidget tests
    """
    def setUp(self):
        ModelFormTest.setUp(self)

    def test_form_meta(self):
        response = self.admin.get(reverse(EDIT_VIEW_NAME))
        self.assertContains(response, 'css/smoothness/jquery-ui-1.8.17.custom.css', count=1)
        self.assertContains(response, 'jquery-ui-1.8.17.custom.min.js', count=1)

    def test_activation(self):
        response = self.admin.get(reverse(EDIT_VIEW_NAME))
        self.assertContains(response, "$('.jqueryuidatepickerwidget').datepicker(", count=2)


    def test_auth_redirect(self):
        pass
    def test_form_post(self):
        pass
    def test_form_validation(self):
        pass




class ReversedFieldsTest(ModelFormTest):
    """
    Check if fields reversed
    """
    def setUp(self):
        ModelFormTest.setUp(self)


    def test_fields_order(self):
        response = self.admin.get(reverse(EDIT_VIEW_NAME))

        html = response.content

        self.assertTrue('<!DOCTYPE HTML>' in html)
        self.assertTrue(html.find('id_bio') < html.find('id_othercontacts') < html.find('id_skype'))



class ListModelsCommandTest(TestCase):
    COMMAND = 'listmodels'

    def test_command_call(self):
        commands_dict = get_commands()
        self.assertTrue(self.COMMAND in commands_dict)
        has_errors = False
        try:
            call_command(self.COMMAND)
        except:
            has_errors = True

        self.assertEqual(has_errors, False)


class SettingsContextProcessorTest(TestCase):
    def test_response(self):
        client = Client()
        response = client.get(reverse(INDEX_VIEW_NAME))
        self.assertEquals(response.context['settings'], settings)


class SettingsDictContextProcessorTest(TestCase):
    def test_response(self):
        client = Client()
        response = client.get(reverse('settings'))
        self.assertEquals(type(response.context['settings_dict']) is dict, True)




class AdminEditLinkTest(TestCase):
    TEMPLATE_SOURCE = '{% load adminlinks %}{% admin_edit_link contact %}'
    VALID_MARKUP = '<a href="/admin/person/contact/1/">(admin)</a>'

    def setUp(self):
        self.template = Template(self.TEMPLATE_SOURCE)
        self.contact = Contact.objects.get(pk=1)
        self.client = Client()


    def test_tag_markup(self):
        markup = self.template.render(Context(dict(contact=self.contact)))
        self.assertEqual(self.VALID_MARKUP, markup)

    def test_no_link(self):
        '''Link must not exist on the index-page for anonymous-user'''
        response = self.client.get(reverse(INDEX_VIEW_NAME))
        self.assertFalse(self.VALID_MARKUP in response.content)

    def test_admin_link_exists(self):
        '''Link must exist on the index for admin-user'''

        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse(INDEX_VIEW_NAME))
        self.assertTrue(self.VALID_MARKUP in response.content)
