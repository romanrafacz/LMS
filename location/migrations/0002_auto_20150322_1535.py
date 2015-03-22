# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='admin_email',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='admin_name',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='admin_phone',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='city',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='country',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='default_tech',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='default_type',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='description',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='location_code',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='notes',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='number_of_rooms',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='owner_code',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='owner_id',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='phone',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='postal_code',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='state',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='street',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='suite',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='tech_email',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='tech_name',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='tech_phone',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='timezone',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwlocationinfo',
            name='web_page',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
