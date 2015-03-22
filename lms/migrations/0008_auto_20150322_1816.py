# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0007_auto_20150322_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avnetdescription',
            old_name='avnet_title',
            new_name='abstract',
        ),
        migrations.RemoveField(
            model_name='avnetdescription',
            name='classroom_delivery_method',
        ),
        migrations.RemoveField(
            model_name='avnetdescription',
            name='created_str',
        ),
        migrations.RemoveField(
            model_name='avnetdescription',
            name='last_modified_by',
        ),
        migrations.RemoveField(
            model_name='avnetdescription',
            name='last_modified_str',
        ),
        migrations.AddField(
            model_name='avnetdescription',
            name='descrtiption',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avnetdescription',
            name='language',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avnetdescription',
            name='overview',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avnetdescription',
            name='prerequisits',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avnetdescription',
            name='topic',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnetdescription',
            name='created',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avnetdescription',
            name='last_modified',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
