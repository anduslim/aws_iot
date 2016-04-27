from django.contrib import admin
from .models import IntakeTime, MedicationIntake, SensorNode, GatewayNode, SensorStickerReading

# Register your models here.


class SensorStickerReadingAdmin(admin.ModelAdmin):
	
	list_display = ('id', 'gw_id', 'sensor_id', 'node_type', 'acc', 'battery_level', 'power', 'server_timestamp', 'gw_timestamp')
	list_filter = ('sensor_id',)

admin.site.register(IntakeTime)
admin.site.register(MedicationIntake)
admin.site.register(GatewayNode)
admin.site.register(SensorNode)
admin.site.register(SensorStickerReading, SensorStickerReadingAdmin)