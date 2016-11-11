# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserIP.user'
        db.delete_column(u'personal_userip', 'user_id')

        # Adding M2M table for field user on 'UserIP'
        m2m_table_name = db.shorten_name(u'personal_userip_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userip', models.ForeignKey(orm[u'personal.userip'], null=False)),
            ('userdata', models.ForeignKey(orm[u'personal.userdata'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userip_id', 'userdata_id'])


        # Changing field 'UserIP.ip'
        db.alter_column(u'personal_userip', 'ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15))

    def backwards(self, orm):
        # Adding field 'UserIP.user'
        db.add_column(u'personal_userip', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['personal.UserData']),
                      keep_default=False)

        # Removing M2M table for field user on 'UserIP'
        db.delete_table(db.shorten_name(u'personal_userip_user'))


        # Changing field 'UserIP.ip'
        db.alter_column(u'personal_userip', 'ip', self.gf('django.db.models.fields.CharField')(max_length=25))

    models = {
        u'personal.userdata': {
            'Meta': {'ordering': "['creation_date']", 'object_name': 'UserData'},
            'counting_logins': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_balance': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'personal.userip': {
            'Meta': {'object_name': 'UserIP'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['personal.UserData']", 'symmetrical': 'False'})
        },
        u'personal.useroperation': {
            'Meta': {'object_name': 'UserOperation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['personal.UserData']"})
        },
        u'personal.userpayment': {
            'Meta': {'object_name': 'UserPayment'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'annotation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['personal.UserData']"})
        }
    }

    complete_apps = ['personal']