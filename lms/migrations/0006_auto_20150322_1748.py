# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_auto_20150322_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classplsummary',
            name='avent_type_info_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='avnet_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='class_prce',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='currency',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='end_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='facility_expense',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='gross_jmw_receipts',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='gross_receipts',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='instructor_expense',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='instructor_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='instructor_name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='instructor_rate',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='jmw_class_info_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='jmw_locaiton_info_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='jmw_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='lab_expense',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='material_expense',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='net_profit',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='other_expense',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='po',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='start_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='total_attend',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='total_expense',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='total_jmw_attend',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classplsummary',
            name='travel_expense',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
    ]
