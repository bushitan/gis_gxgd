# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0010_auto_20201011_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='broadcast',
            field=models.ManyToManyField(to='lite.Broadcast', null=True, blank=True),
        ),
    ]
