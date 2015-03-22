# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_auto_20150322_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='avnet_type_info_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='avnet_type_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='category',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='class_status',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='created_str',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='currency',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='duration_unit',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='end_date_str',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='gtr',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='instructor',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='instructor_name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='jmw_locaiton_info_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='jmw_name',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='labs',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='last_modified_by',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='last_modified_str',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='lock_price',
            field=models.CharField(max_length=1, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='notes',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='owned_by',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='po',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='price',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='public',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='room_info_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='source_by',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='start_date_str',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='subcategory',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='tech',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='title',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='total_jmw_registered',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='total_registered',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jmwclassinfo',
            name='type_url',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
