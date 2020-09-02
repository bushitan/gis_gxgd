# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0007_auto_20200831_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='area_code',
            field=models.CharField(default=b'', max_length=32, null=True, verbose_name='STB\u533a\u57df\u7801', blank=True),
        ),
    ]
