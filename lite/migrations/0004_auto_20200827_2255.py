# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0003_auto_20200827_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=32, null=True, verbose_name='\u540d\u5b57', blank=True)),
                ('admin_name', models.CharField(default=b'', max_length=32, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u5b57', blank=True)),
                ('uuid', models.CharField(default=b'', max_length=36, null=True, verbose_name='uuid', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('latitude', models.FloatField(default=0, null=True, verbose_name='\u7eac\u5ea6', blank=True)),
                ('longitude', models.FloatField(default=0, null=True, verbose_name='\u7ecf\u5ea6', blank=True)),
                ('tag', models.IntegerField(default=0, verbose_name='\u533a\u57df\u6807\u7b7e')),
                ('father', models.ForeignKey(verbose_name='\u6240\u5c5e\u533a\u57df', blank=True, to='lite.Address', null=True)),
            ],
            options={
                'verbose_name': '\u533a\u57df',
                'verbose_name_plural': '\u533a\u57df',
            },
        ),
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=32, null=True, verbose_name='\u540d\u5b57', blank=True)),
                ('admin_name', models.CharField(default=b'', max_length=32, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u5b57', blank=True)),
                ('uuid', models.CharField(default=b'', max_length=36, null=True, verbose_name='uuid', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('episode_list', models.TextField(null=True, verbose_name='\u5267\u96c6\u65f6\u95f4\u8868', blank=True)),
                ('tag', models.IntegerField(default=0, verbose_name='\u8282\u76ee\u6807\u7b7e')),
            ],
            options={
                'verbose_name': '\u8282\u76ee',
                'verbose_name_plural': '\u8282\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=32, null=True, verbose_name='\u540d\u5b57', blank=True)),
                ('admin_name', models.CharField(default=b'', max_length=32, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u5b57', blank=True)),
                ('uuid', models.CharField(default=b'', max_length=36, null=True, verbose_name='uuid', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('tag', models.IntegerField(default=0, verbose_name='\u9891\u9053\u6807\u7b7e')),
            ],
            options={
                'verbose_name': '\u9891\u9053',
                'verbose_name_plural': '\u9891\u9053',
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=32, null=True, verbose_name='\u540d\u5b57', blank=True)),
                ('admin_name', models.CharField(default=b'', max_length=32, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u5b57', blank=True)),
                ('uuid', models.CharField(default=b'', max_length=36, null=True, verbose_name='uuid', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('rate', models.FloatField(default=0, verbose_name='\u6536\u89c6\u7387')),
                ('uv', models.IntegerField(default=0, verbose_name='\u8bbf\u95ee\u4eba\u6570')),
                ('pv', models.IntegerField(default=0, verbose_name='\u8bbf\u95ee\u6b21\u6570')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('tag', models.IntegerField(default=0, verbose_name='\u5267\u96c6\u6807\u7b7e')),
                ('address', models.ForeignKey(verbose_name='\u6240\u5c5e\u8282\u76ee', blank=True, to='lite.Address', null=True)),
                ('boadcast', models.ForeignKey(verbose_name='\u6240\u5c5e\u8282\u76ee', blank=True, to='lite.Broadcast', null=True)),
            ],
            options={
                'verbose_name': '\u5267\u96c6',
                'verbose_name_plural': '\u5267\u96c6',
            },
        ),
        migrations.AddField(
            model_name='broadcast',
            name='channel',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u9891\u9053', blank=True, to='lite.Channel', null=True),
        ),
    ]
