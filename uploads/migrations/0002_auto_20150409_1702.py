# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part',
            old_name='jmw_name',
            new_name='mw_name',
        ),
    ]
