# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0004_auto_20200827_2255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='broadcast',
            options={'verbose_name': '2\u3001\u8282\u76ee', 'verbose_name_plural': '2\u3001\u8282\u76ee'},
        ),
        migrations.AlterModelOptions(
            name='channel',
            options={'verbose_name': '1\u3001\u9891\u9053', 'verbose_name_plural': '1\u3001\u9891\u9053'},
        ),
        migrations.AlterModelOptions(
            name='episode',
            options={'verbose_name': '3\u3001\u5267\u96c6', 'verbose_name_plural': '3\u3001\u5267\u96c6'},
        ),
        migrations.AlterField(
            model_name='episode',
            name='address',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u533a\u57df', blank=True, to='lite.Address', null=True),
        ),
    ]
