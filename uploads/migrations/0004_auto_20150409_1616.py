# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_auto_20150409_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='jmw_name',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
