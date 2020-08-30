# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0006_auto_20200828_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='boadcast',
            new_name='broadcast',
        ),
    ]
