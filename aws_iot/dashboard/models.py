from __future__ import unicode_literals, absolute_import

from django.db import models
from . import managers
from aws_iot.users.models import User


class IntakeTime(models.Model):

    intake_time = models.TimeField(('Expected Intake Time'), blank=True, null=True)


    def __str__(self):
        return ', '.join([str(self.intake_time)])


class MedicationIntake(models.Model):

    modified_timestamp = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User)

    contents = models.TextField(blank=True, null=True)
    expected_intake = models.ForeignKey(IntakeTime, blank=True, null=True)

    objects = managers.MedicationIntakeManager()
    
    class Meta:
        verbose_name = 'Medication Intake'
        verbose_name_plural = 'Medication Intake'

    def __str__(self):
        return ', '.join([str(self.user), str(self.expected_intake.intake_time)])


class NodeMetaData(models.Model):
    ''' Node MetaData Abstract
    '''

    modified_timestamp = models.DateTimeField(auto_now=True)

    NODE_TYPE_CHOICES = (
        (1, 'Gateway'),
        (2, 'Sensor-ReedSwitch'),
        (3, 'Sensor-EstimoteStickers'),
        (0, 'Others'),
    )

    node_type = models.IntegerField(choices=NODE_TYPE_CHOICES, default=0)
    node_id = models.IntegerField(('Node ID'), unique=True)
    node_desc = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        abstract = True


class GatewayNode(NodeMetaData):

    user2 = models.ForeignKey(User, blank=True, null=True)

    objects = managers.GatewayNodeManager()

    class Meta:
        verbose_name = 'Gateway Node'
        verbose_name_plural = 'Gateway Node'

    def save(self, **kwargs):
        self.node_type = 1
        super(GatewayNode, self).save()

    def __str__(self):
        return ', '.join([str(self.node_id)])


class SensorNode(NodeMetaData):

    uuid = models.UUIDField(('UUID'), blank=True, null=True)
    medication_intake = models.ForeignKey(MedicationIntake, blank=True, null=True)

    objects = managers.SensorNodeManager()

    class Meta:
        verbose_name = 'Sensor Node'
        verbose_name_plural = 'Sensor Node'


    def __str__(self):
        return ', '.join([str(self.node_id)])


class ReadingMetaData(models.Model):

    modified_timestamp = models.DateTimeField(auto_now=True)

    gw_id = models.ForeignKey(GatewayNode, blank=True, null=True)
    
    server_timestamp = models.DateTimeField(blank=True, null=True)
    gw_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class SensorStickerReading(ReadingMetaData):

    # should check if is estimote sticker type?
    sensor_id = models.ForeignKey(SensorNode)

    acc_x = models.FloatField(default=0.0)
    acc_y = models.FloatField(default=0.0)
    acc_z = models.FloatField(default=0.0)

    battery_level = models.CharField(max_length=16, blank=False)
    power = models.IntegerField(default=1)

    objects = managers.SensorStickerReadingManager()

    class Meta:
        verbose_name = 'Sensor (Estimote Sticker) Reading'
        verbose_name_plural = 'Sensor (Estimote Sticker) Reading'

    def node_type(self):
        return self.sensor_id.node_type
    node_type.short_description = 'Sensor Type'

    def acc(self):
        return ', '.join([str(self.acc_x), str(self.acc_y), str(self.acc_z)])
    acc.short_description = 'Accelerometer'

    def __str__(self):
        return ', '.join([str(self.sensor_id)])





