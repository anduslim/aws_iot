# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20160427_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicationintake',
            options={'verbose_name': '*Medication Intake', 'verbose_name_plural': '*Medication Intake'},
        ),
        migrations.AddField(
            model_name='medicationintake',
            name='timing_threshold_min',
            field=models.IntegerField(default=2, verbose_name='Threshold (min)'),
        ),
    ]
