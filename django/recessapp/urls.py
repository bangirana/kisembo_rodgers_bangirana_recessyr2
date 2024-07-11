from django.urls import path
from . import views

urlpatterns = [
    path('', views.soilMoistureReading, name='soil_moisture_reading'),
    path('soil_moisture_detail/<str:id>', views.soilMoistureReading, name='soil_moisture_reading'),
]