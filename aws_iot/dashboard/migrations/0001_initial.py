# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IntakeTime',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('intake_time', models.TimeField(null=True, blank=True, verbose_name='Expected Intake Time')),
            ],
        ),
        migrations.CreateModel(
            name='MedicationIntake',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('modified_timestamp', models.DateTimeField(auto_now=True)),
                ('contents', models.TextField(null=True, blank=True)),
                ('expected_intake', models.ForeignKey(null=True, to='dashboard.IntakeTime', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Medication Intake',
                'verbose_name': 'Medication Intake',
            },
        ),
        migrations.CreateModel(
            name='SensorNode',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('modified_timestamp', models.DateTimeField(auto_now=True)),
                ('node_type', models.IntegerField(choices=[(1, 'Gateway'), (2, 'Sensor-ReedSwitch'), (3, 'Sensor-EstimoteStickers'), (0, 'Others')], default=0)),
                ('node_id', models.IntegerField(unique=True, verbose_name='Node ID')),
                ('node_desc', models.CharField(null=True, max_length=32, blank=True)),
                ('uuid', models.UUIDField(null=True, blank=True, verbose_name='UUID')),
                ('medication_intake', models.ForeignKey(null=True, to='dashboard.MedicationIntake', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Sensor Node',
                'verbose_name': 'Sensor Node',
            },
        ),
    ]
