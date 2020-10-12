# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0013_auto_20201012_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='code',
            field=models.IntegerField(default=0, verbose_name='\u9891\u9053\u4ee3\u7801'),
        ),
    ]
