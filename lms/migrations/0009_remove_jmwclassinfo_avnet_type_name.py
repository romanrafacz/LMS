# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0008_auto_20150322_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jmwclassinfo',
            name='avnet_type_name',
        ),
    ]
