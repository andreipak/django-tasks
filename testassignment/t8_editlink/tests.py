from django.test import TestCase
from testassignment.t1_contact.models import Contact
from django.template import Template, Context
from django.test.client import Client
from django.core.urlresolvers import reverse

TEMPLATE_SOURCE = '{% load adminlinks %}{% admin_edit_link contact %}'
VALID_MARKUP = '<a href="/admin/t1_contact/contact/1/">(admin)</a>'
VIEW_NAME='index'

class AdminEditLinkTest(TestCase):
    def setUp(self):
        self.template = Template(TEMPLATE_SOURCE)
        self.contact = Contact.objects.get(pk=1)


    def test_tag_markup(self):
        markup = self.template.render(Context(dict(contact=self.contact)))
        self.assertEqual(VALID_MARKUP, markup)


class MainPageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_no_link(self):
        response = self.client.get(reverse(VIEW_NAME))
        self.assertFalse(VALID_MARKUP in response.content)

    def test_admin_link_exists(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse(VIEW_NAME))
        self.assertTrue(VALID_MARKUP in response.content)
