from django.contrib import admin
# from .models import IntakeTime, MedicationIntake, SensorNode, GatewayNode, SensorStickerReading
from .models import MedicationIntake, SensorNode, SensorStickerReading, DerivedIntakeReading

# Register your models here.

class SensorStickerReadingAdmin(admin.ModelAdmin):	
	list_display = ('id', 'sensor_id', 'acc', 'battery_level', 'power', 'server_timestamp')

class DerivedIntakeReadingAdmin(admin.ModelAdmin):	
	list_display = ('id', 'sensor_id', 'isOpen', 'server_timestamp')

admin.site.register(MedicationIntake)
admin.site.register(SensorNode)
admin.site.register(SensorStickerReading, SensorStickerReadingAdmin)
admin.site.register(DerivedIntakeReading, DerivedIntakeReadingAdmin)