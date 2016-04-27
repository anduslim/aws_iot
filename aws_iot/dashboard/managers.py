from django.db import models, IntegrityError


class MedicationIntakeManager(models.Manager):

	def get_timing(self, source=None, destination=None):

	    try:
	        readings = self.model.objects.get()
	    except self.model.DoesNotExist:
	        readings = False

	    return readings

class SensorNodeManager(models.Manager):

	def get_sensor(self, node_id):
		print(node_id)
		node = self.model.objects.get(node_id=node_id)

		return node

	def create_sensor(self, payload):

		print(payload)

		try:
			mapping = self.create(node_type=payload['node_type'], node_id=payload['node_id'], uuid=payload['uuid'], medication_intake=payload['medication_intake'])
		except IntegrityError as e:
			return 0

		return 1

class GatewayNodeManager(models.Manager):

	def create_gateway(self, payload):

		print(payload)

		try:
			mapping = self.create(node_type=payload['node_type'], node_id=payload['node_id'], user=payload['user'])
		except IntegrityError as e:
			return 0

		return 1

class SensorStickerReadingManager(models.Manager):

	def create_reading(self, payload):

		print(payload)

		try:
			reading = self.create(gw_id=payload['gw_id'], server_timestamp=payload['server_timestamp'], gw_timestamp=payload['gw_timestamp'], sensor_id=payload['sensor_id'], acc_x=payload['acc_x'], acc_y=payload['acc_y'], acc_z=payload['acc_z'], battery_level=payload['battery_level'], power=payload['power'])
		except IntegrityError as e:
			return 0

		return 1

class DerivedIntakeReadingManager(models.Manager):

	def create_reading(self, payload):

		print(payload)


		try:
			reading = self.create(sensor_id=payload['sensor_id'], isOpen=payload['isOpen'])
		except IntegrityError as e:
			return 0

		return 1