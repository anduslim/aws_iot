# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_gatewaynode_sensorstickerreading'),
    ]

    operations = [
        migrations.CreateModel(
            name='DerivedIntakeReading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modified_timestamp', models.DateTimeField(auto_now=True)),
                ('server_timestamp', models.DateTimeField(null=True, blank=True)),
                ('isOpen', models.NullBooleanField(verbose_name='Opened')),
            ],
            options={
                'verbose_name': 'Derived Intake Reading',
                'verbose_name_plural': 'Derived Intake Reading',
            },
        ),
        migrations.RemoveField(
            model_name='gatewaynode',
            name='user2',
        ),
        migrations.RemoveField(
            model_name='medicationintake',
            name='expected_intake',
        ),
        migrations.RemoveField(
            model_name='medicationintake',
            name='user',
        ),
        migrations.RemoveField(
            model_name='sensornode',
            name='medication_intake',
        ),
        migrations.RemoveField(
            model_name='sensorstickerreading',
            name='gw_id',
        ),
        migrations.RemoveField(
            model_name='sensorstickerreading',
            name='gw_timestamp',
        ),
        migrations.AddField(
            model_name='medicationintake',
            name='expected_intake_timing',
            field=models.TimeField(null=True, verbose_name='Expected Intake Time', blank=True),
        ),
        migrations.AddField(
            model_name='medicationintake',
            name='med_desc',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sensornode',
            name='medication_intake_list',
            field=models.ManyToManyField(to='dashboard.MedicationIntake', null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='GatewayNode',
        ),
        migrations.DeleteModel(
            name='IntakeTime',
        ),
        migrations.AddField(
            model_name='derivedintakereading',
            name='sensor_id',
            field=models.ForeignKey(to='dashboard.SensorNode'),
        ),
    ]
