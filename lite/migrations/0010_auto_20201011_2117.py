# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0009_user_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=32, null=True, verbose_name='\u5bc6\u7801', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32, null=True, verbose_name='\u8d26\u53f7', blank=True),
        ),
    ]
