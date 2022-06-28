from django.urls import path
from measurement.views import \
    SensorListView, \
    SensorDetailView, \
    SensorCreateView, \
    SensorRetrieveUpdateView, \
    MeasurementCreateView

urlpatterns = [
    path('sensor/list', SensorListView.as_view()),
    path('sensor/detail', SensorDetailView.as_view()),
    path('sensor/create', SensorCreateView.as_view()),
    path('sensor/update/<pk>/', SensorRetrieveUpdateView.as_view()),
    path('measurement/create', MeasurementCreateView.as_view())
]
