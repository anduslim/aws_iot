# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GatewayNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('modified_timestamp', models.DateTimeField(auto_now=True)),
                ('node_type', models.IntegerField(default=0, choices=[(1, 'Gateway'), (2, 'Sensor-ReedSwitch'), (3, 'Sensor-EstimoteStickers'), (0, 'Others')])),
                ('node_id', models.IntegerField(unique=True, verbose_name='Node ID')),
                ('node_desc', models.CharField(max_length=32, null=True, blank=True)),
                ('user2', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'Gateway Node',
                'verbose_name': 'Gateway Node',
            },
        ),
        migrations.CreateModel(
            name='SensorStickerReading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('modified_timestamp', models.DateTimeField(auto_now=True)),
                ('server_timestamp', models.DateTimeField(null=True, blank=True)),
                ('gw_timestamp', models.DateTimeField(null=True, blank=True)),
                ('acc_x', models.FloatField(default=0.0)),
                ('acc_y', models.FloatField(default=0.0)),
                ('acc_z', models.FloatField(default=0.0)),
                ('battery_level', models.CharField(max_length=16)),
                ('power', models.IntegerField(default=1)),
                ('gw_id', models.ForeignKey(blank=True, to='dashboard.GatewayNode', null=True)),
                ('sensor_id', models.ForeignKey(to='dashboard.SensorNode')),
            ],
            options={
                'verbose_name_plural': 'Sensor (Estimote Sticker) Reading',
                'verbose_name': 'Sensor (Estimote Sticker) Reading',
            },
        ),
    ]
