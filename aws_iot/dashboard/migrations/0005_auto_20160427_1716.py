# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20160427_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicationintake',
            name='timing_threshold_min',
        ),
        migrations.AddField(
            model_name='sensornode',
            name='timing_threshold_min',
            field=models.IntegerField(default=2, verbose_name='Threshold (min)'),
        ),
    ]
