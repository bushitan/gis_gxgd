# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0002_auto_20200827_2233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
        migrations.AddField(
            model_name='user',
            name='admin_name',
            field=models.CharField(default=b'', max_length=32, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u5b57', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=b'', max_length=32, null=True, verbose_name='\u540d\u5b57', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.CharField(default=b'', max_length=36, null=True, verbose_name='uuid', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='expires',
            field=models.FloatField(null=True, verbose_name='expires', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='logo',
            field=models.CharField(default=b'', max_length=300, null=True, verbose_name='logo', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nick_name',
            field=models.CharField(max_length=100, null=True, verbose_name='\u6635\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=40, null=True, verbose_name='\u7535\u8bdd', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='session',
            field=models.CharField(max_length=128, null=True, verbose_name='session', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wx_expires_in',
            field=models.FloatField(null=True, verbose_name='\u5fae\u4fe1SessionKey', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wx_id',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5fae\u4fe1id', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wx_open_id',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5fae\u4fe1OpenID', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wx_session_key',
            field=models.CharField(max_length=128, null=True, verbose_name='\u5fae\u4fe1SessionKey', blank=True),
        ),
    ]
