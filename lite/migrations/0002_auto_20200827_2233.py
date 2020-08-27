# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '\u9422\u3126\u57db_\u9369\u70d8\u6e70\u6dc7\u2103\u4f05', 'verbose_name_plural': '\u9422\u3126\u57db_\u9369\u70d8\u6e70\u6dc7\u2103\u4f05'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='user',
            name='expires',
            field=models.FloatField(null=True, verbose_name='Django\u9428\u5246ession\u6769\u56e8\u6e61\u93c3\u5815\u68ff', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='logo',
            field=models.CharField(default=b'', max_length=300, null=True, verbose_name='logo\u95be\u70ac\u5e34', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nick_name',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5bf0\ue1bb\u4fca\u93c4\u7535\u041e', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=40, null=True, verbose_name='\u93b5\u5b2b\u6e80', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='session',
            field=models.CharField(max_length=128, null=True, verbose_name='Django\u9428\u5246ession', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wx_expires_in',
            field=models.FloatField(null=True, verbose_name='\u5bf0\ue1bb\u4fcaSessionKey\u6769\u56e8\u6e61\u93c3\u5815\u68ff', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wx_id',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5bf0\ue1bb\u4fca\u9359\ufffd', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wx_open_id',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5bf0\ue1bb\u4fcaOpenID', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wx_session_key',
            field=models.CharField(max_length=128, null=True, verbose_name='\u5bf0\ue1bb\u4fcaSessionKey', blank=True),
        ),
    ]
