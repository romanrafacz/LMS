# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roominfo',
            name='location_info_id',
        ),
        migrations.DeleteModel(
            name='JMWLocationInfo',
        ),
        migrations.DeleteModel(
            name='RoomInfo',
        ),
    ]
