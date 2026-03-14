from django.shortcuts import render
from f1_race_hub.drivers.models import Driver

def index(request):
    drivers_count = Driver.objects.count()

    context = {
        "drivers_count": drivers_count,
    }

    return render(request, "index.html", context)