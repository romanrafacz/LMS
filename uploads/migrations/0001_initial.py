# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jmw_name', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
