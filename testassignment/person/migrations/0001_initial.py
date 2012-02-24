# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Contact'
        db.create_table('person_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dateofbirth', self.gf('django.db.models.fields.DateField')(db_index=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=1, blank=1)),
            ('contacts', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50, null=1, blank=1)),
            ('othercontacts', self.gf('django.db.models.fields.TextField')(null=1, blank=1)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=1, blank=1)),
        ))
        db.send_create_signal('person', ['Contact'])


    def backwards(self, orm):
        
        # Deleting model 'Contact'
        db.delete_table('person_contact')


    models = {
        'person.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {'null': '1', 'blank': '1'}),
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dateofbirth': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'othercontacts': ('django.db.models.fields.TextField', [], {'null': '1', 'blank': '1'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': '1', 'blank': '1'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': '1', 'blank': '1'})
        }
    }

    complete_apps = ['person']
