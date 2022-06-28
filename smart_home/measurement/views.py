from measurement.models import Sensor, Measurement
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer, MeasurementCreateSerializer

class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorDetailView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class SensorCreateView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer