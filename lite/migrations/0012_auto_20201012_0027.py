# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0011_user_broadcast'),
    ]

    operations = [
        migrations.AddField(
            model_name='broadcast',
            name='desc',
            field=models.CharField(max_length=50, null=True, verbose_name='\u8bf4\u660e', blank=True),
        ),
        migrations.AddField(
            model_name='broadcast',
            name='range_time',
            field=models.CharField(max_length=50, null=True, verbose_name='\u67e5\u8be2\u65f6\u95f4\u8303\u56f4', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='broadcast',
            field=models.ManyToManyField(to='lite.Broadcast', null=True, verbose_name='\u53ef\u67e5\u770b\u7684\u8282\u76ee', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='channel',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u536b\u89c6\u9891\u9053', blank=True, to='lite.Channel', null=True),
        ),
    ]
