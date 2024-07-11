from django.shortcuts import render
from .models import SoilMoistureReading

# Create your views here.
def soilMoistureReading(request):
    soil_readings = SoilMoistureReading.objects.all()
    context = {
        'soil_readings': soil_readings
        }
    return render(request, 'soil_moisture_reading.html', context)

def soilMoistureDetailView(request, id):
    soil_reading = SoilMoistureReading.objects.get(pk=id).order_by('-timestamp')
    context = {
        'soil_reading': soil_reading
        }
    return render(request, 'soil_moisture_detail.html', context)