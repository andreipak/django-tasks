# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'HttpRequestLogEntry'
        db.create_table('t3_httplog_httprequestlogentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('request_method', self.gf('django.db.models.fields.CharField')(max_length=6, db_index=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('query_string', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('t3_httplog', ['HttpRequestLogEntry'])


    def backwards(self, orm):
        
        # Deleting model 'HttpRequestLogEntry'
        db.delete_table('t3_httplog_httprequestlogentry')


    models = {
        't3_httplog.httprequestlogentry': {
            'Meta': {'object_name': 'HttpRequestLogEntry'},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'query_string': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '6', 'db_index': 'True'})
        }
    }

    complete_apps = ['t3_httplog']
