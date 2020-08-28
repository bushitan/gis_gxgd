# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0005_auto_20200827_2311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['create_time'], 'verbose_name': '\u533a\u57df', 'verbose_name_plural': '\u533a\u57df'},
        ),
        migrations.AddField(
            model_name='episode',
            name='code',
            field=models.IntegerField(default=-1, verbose_name='\u8282\u76eecode'),
        ),
    ]
