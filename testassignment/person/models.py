from django.db import models
from django.forms import ModelForm

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField('Date of birth',db_index=True)
    bio = models.TextField('Bio', null=1, blank=1)
    email = models.EmailField('Email')
    jabber = models.EmailField('Jabber ID')
    skype = models.CharField('Skype ID', max_length=50, null=1, blank=1)
    other_contacts = models.TextField('Other contacts', null=1, blank=1)
    photo = models.ImageField(upload_to='photo', null=1, blank=1)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
