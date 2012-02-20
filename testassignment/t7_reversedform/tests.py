from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from testassignment.t6_widgetsjquery.tests import ModelFormTest

VIEW_NAME = 'editmodel_reversed'

class ReversedFieldsTest(ModelFormTest):
    """
    Check if fields reversed
    """
    def setUp(self):
        ModelFormTest.setUp(self)


    def test_fields_order(self):
        response = self.admin.get(reverse(VIEW_NAME))

        html = response.content

        self.assertTrue('<!DOCTYPE HTML>' in html)
        self.assertTrue(html.find('id_bio') < html.find('id_othercontacts') < html.find('id_skype'))
