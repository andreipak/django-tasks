# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column('person_contact', 'name', 'first_name')
        db.rename_column('person_contact', 'lastname', 'last_name')
        db.rename_column('person_contact', 'dateofbirth', 'dob')
        db.rename_column('person_contact', 'othercontacts','other_contacts')
        db.delete_column('person_contact', 'contacts')




    def backwards(self, orm):
        # User chose to not deal with backwards NULL issues for 'Contact.contacts'
        raise RuntimeError("Cannot reverse this migration. 'Contact.contacts' and its values cannot be restored.")

    models = {
        'person.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {'null': '1', 'blank': '1'}),
            'dob': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'null': '1', 'blank': '1'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': '1', 'blank': '1'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': '1', 'blank': '1'})
        }
    }

    complete_apps = ['person']
