# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'HttpRequestLogEntry.priority'
        db.add_column('t3_httplog_httprequestlogentry', 'priority', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'HttpRequestLogEntry.priority'
        db.delete_column('t3_httplog_httprequestlogentry', 'priority')


    models = {
        't3_httplog.httprequestlogentry': {
            'Meta': {'object_name': 'HttpRequestLogEntry'},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'query_string': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '6', 'db_index': 'True'})
        }
    }

    complete_apps = ['t3_httplog']
