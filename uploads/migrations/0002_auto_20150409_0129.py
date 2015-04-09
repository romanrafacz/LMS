# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0009_remove_jmwclassinfo_avnet_type_name'),
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='training_id',
        ),
        migrations.AddField(
            model_name='part',
            name='avnet_type_name',
            field=models.ForeignKey(default=1, to='lms.JMWClassInfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
