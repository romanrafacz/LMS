# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_auto_20150322_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='end_date_local',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='last_modified',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='start_date_local',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
