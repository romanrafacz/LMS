# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20150317_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='create',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='location',
            field=models.CharField(default=datetime.datetime(2015, 3, 27, 15, 58, 40, 903968, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='serial',
            field=models.CharField(default=datetime.datetime(2015, 3, 27, 15, 58, 49, 482873, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
