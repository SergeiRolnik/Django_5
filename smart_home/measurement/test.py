# from rest_framework.renderers import JSONRenderer
from models import Sensor
from serializers import SensorSerializer
sensor = Sensor.objects.first()
serializer = SensorSerializer(sensor)
print(serializer.data)
# JSONRenderer().render(serializer.data)