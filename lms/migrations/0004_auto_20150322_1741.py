# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_auto_20150322_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='created',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='duration',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
