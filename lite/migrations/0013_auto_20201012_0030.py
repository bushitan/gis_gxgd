# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0012_auto_20201012_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcast',
            name='desc',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name='\u8bf4\u660e', blank=True),
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='range_time',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name='\u67e5\u8be2\u65f6\u95f4\u8303\u56f4', blank=True),
        ),
    ]
