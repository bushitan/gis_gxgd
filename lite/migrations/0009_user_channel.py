# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0008_address_area_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='channel',
            field=models.ForeignKey(verbose_name='\u6240\u53ef\u4ee5\u89c2\u770b\u7684\u9891\u9053', blank=True, to='lite.Channel', null=True),
        ),
    ]
