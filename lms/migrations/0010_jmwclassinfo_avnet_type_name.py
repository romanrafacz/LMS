# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0009_remove_jmwclassinfo_avnet_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='jmwclassinfo',
            name='avnet_type_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
