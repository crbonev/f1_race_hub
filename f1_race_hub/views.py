from django.shortcuts import render
from f1_race_hub.drivers.models import Driver
from f1_race_hub.races.models import Race
from f1_race_hub.teams.models import Team


def index(request):
    drivers_count = Driver.objects.count()
    teams_count = Team.objects.count()
    races_count = Race.objects.count()

    context = {
        "drivers_count": drivers_count,
        "teams_count": teams_count,
        "races_count": races_count,
    }

    return render(request, "index.html", context)