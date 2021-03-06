# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PageText'
        db.create_table(u'lesnoe_pagetext', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text1', self.gf('ckeditor.fields.RichTextField')()),
        ))
        db.send_create_signal(u'lesnoe', ['PageText'])


    def backwards(self, orm):
        # Deleting model 'PageText'
        db.delete_table(u'lesnoe_pagetext')


    models = {
        u'lesnoe.gallery': {
            'Meta': {'ordering': "['sort']", 'object_name': 'Gallery'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'sort': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'lesnoe.pagetext': {
            'Meta': {'object_name': 'PageText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text1': ('ckeditor.fields.RichTextField', [], {})
        },
        u'lesnoe.project': {
            'Meta': {'object_name': 'Project'},
            'area_2nd_fl': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'area_garage': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'area_living': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'area_total': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'house_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_plot_length': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'min_plot_width': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'place_in_line': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'roof_angle': ('django.db.models.fields.IntegerField', [], {}),
            'volume': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'z500_id': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        u'lesnoe.projectimg': {
            'Meta': {'object_name': 'ProjectImg'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lesnoe.Project']"})
        }
    }

    complete_apps = ['lesnoe']