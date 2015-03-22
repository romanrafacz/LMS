# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_auto_20150322_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avnetdescription',
            name='avnet_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnetdescription',
            name='avnet_title',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnetdescription',
            name='classroom_delivery_method',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnetdescription',
            name='created',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnetdescription',
            name='created_str',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnetdescription',
            name='last_modified',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnetdescription',
            name='last_modified_by',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnetdescription',
            name='last_modified_str',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnettypeinfo',
            name='avnet_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnettypeinfo',
            name='avnet_title',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnettypeinfo',
            name='classroom_delivery_method',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnettypeinfo',
            name='created',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnettypeinfo',
            name='created_str',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnettypeinfo',
            name='last_modified',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnettypeinfo',
            name='last_modified_by',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnettypeinfo',
            name='last_modified_str',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
    ]
