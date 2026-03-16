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
    race = get_object_or_404(Race, pk=pk)

    return render(
        request,
        'races/race-details.html',
        {'race': race}
    )


def race_create(request):
    if request.method == 'POST':
        form = RaceCreateForm(request.POST)

        if form.is_valid():
            race = form.save()
            return redirect('race-details', pk=race.pk)
    else:
        form = RaceCreateForm()

    return render(
        request,
        'races/race-create.html',
        {'form': form}
    )


def add_driver_to_race(request, pk):
    race = get_object_or_404(Race, pk=pk)

    if request.method == 'POST':
        form = RaceResultForm(request.POST)

        if form.is_valid():
            race_result = form.save(commit=False)
            race_result.race = race
            race_result.save()
            return redirect('race-details', pk=race.pk)
    else:
        form = RaceResultForm()

    return render(
        request,
        'races/add-driver.html',
        {
            'race': race,
            'form': form,
        }
    )