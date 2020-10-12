# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0014_channel_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='broadcast',
            name='index_name',
            field=models.CharField(default=b'RTG', max_length=32, verbose_name='\u5927\u6570\u636e\u5206\u6790\u7c7b\u578b', choices=[(b'SHR', '\u5e02\u573a\u5360\u6709\u7387'), (b'AUDDURATION', '\u6536\u89c6\u65f6\u957f'), (b'RTG', '\u6536\u89c6\u7387'), (b'RTG000', '\u6536\u89c6\u673a\u9876\u76d2\u6570'), (b'TAUD', '\u5e73\u5747\u6536\u89c6\u65f6\u957f')]),
        ),
    ]
