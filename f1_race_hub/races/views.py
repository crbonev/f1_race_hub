from django.shortcuts import render, get_object_or_404, redirect
from .models import Race
from .forms import RaceCreateForm, RaceResultForm


def races_list(request):
    races = Race.objects.all()

    return render(
        request,
        'races/races-list.html',
        {'races': races}
    )


def race_details(request, pk):
    return render(request, 'races/race-details.html', {'race': Race.objects.get(pk=pk)})


def race_create(request):
    return render(request, 'races/race-create.html')


def add_driver_to_race(request, pk):
    return render(request, 'races/race-create.html', {'race': Race.objects.get(pk=pk)})