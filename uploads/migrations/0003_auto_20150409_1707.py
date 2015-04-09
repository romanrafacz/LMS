# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_auto_20150409_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part',
            old_name='mw_name',
            new_name='jmw_name',
        ),
    ]
