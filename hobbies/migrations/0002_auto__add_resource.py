# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resource'
        db.create_table('hobbies_resource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hobby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hobbies.Hobby'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('hobbies', ['Resource'])


    def backwards(self, orm):
        # Deleting model 'Resource'
        db.delete_table('hobbies_resource')


    models = {
        'hobbies.hobby': {
            'Meta': {'object_name': 'Hobby'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'hobbies.resource': {
            'Meta': {'object_name': 'Resource'},
            'hobby': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hobbies.Hobby']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['hobbies']