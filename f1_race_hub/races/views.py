from django.shortcuts import render

from f1_race_hub.races.models import Race


# Create your views here.
def races_list(request):
    races = Race.objects.all()
    return render(request, 'races/races-list.html', {'races': races})


def race_create(request):
    return render(request, 'races/race-create.html')

def race_details(request, pk):
    race = Race.objects.get(pk=pk)
    return render(request, 'races/race-details.html', {'race': race})