# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpeakerCertification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('speaker_cert_id', models.IntegerField()),
                ('avnet_type_id', models.IntegerField(null=True)),
                ('jmw_course_info_id', models.IntegerField(null=True)),
                ('cert_languate', models.CharField(max_length=10, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpeakerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('speaker_info_id', models.IntegerField()),
                ('hourly_rate', models.DecimalField(null=True, max_digits=6, decimal_places=2)),
                ('weekly_rate', models.DecimalField(null=True, max_digits=6, decimal_places=2)),
                ('currency', models.CharField(max_length=10, null=True)),
                ('bio', models.TextField(null=True)),
                ('address_1', models.CharField(max_length=100, null=True)),
                ('address_2', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('postal_code', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=20, null=True)),
                ('contact_id', models.IntegerField(null=True)),
                ('contact_type', models.CharField(max_length=20, null=True)),
                ('prefix', models.CharField(max_length=20, null=True)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('suffix', models.CharField(max_length=20, null=True)),
                ('nickname', models.CharField(max_length=25, null=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('company_id', models.IntegerField(null=True)),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('home_phone', models.CharField(max_length=20, null=True)),
                ('office_phone', models.CharField(max_length=20, null=True)),
                ('mobile_phone', models.CharField(max_length=20, null=True)),
                ('fax', models.CharField(max_length=20, null=True)),
                ('last_contact', models.IntegerField(null=True)),
                ('referred_by', models.CharField(max_length=50, null=True)),
                ('notes', models.TextField(null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('email_2', models.CharField(max_length=100, null=True)),
                ('speaker_active', models.CharField(max_length=1, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='speakercertification',
            name='speaker_info_id',
            field=models.ForeignKey(to='speaker.SpeakerInfo'),
            preserve_default=True,
        ),
    ]
