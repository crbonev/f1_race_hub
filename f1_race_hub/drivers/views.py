from django.shortcuts import render, redirect, get_object_or_404
from .models import Driver
from .forms import CreateDriverForm, DriverEditForm
from f1_race_hub.teams.models import Team


def drivers_list(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/drivers-list.html', {'drivers': drivers})


def driver_details(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, 'drivers/driver-details.html', {'driver': driver})


def driver_create(request):
    if request.method == "POST":
        form = CreateDriverForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('drivers-list')

    else:
        form = CreateDriverForm()

    return render(request, 'drivers/driver-create.html', {'form': form})


def driver_edit(request, pk):
    driver = get_object_or_404(Driver, pk=pk)

    if request.method == "POST":
        form = DriverEditForm(request.POST, instance=driver)

        if form.is_valid():
            form.save()
            return redirect('driver-details', pk)

    else:
        form = DriverEditForm(instance=driver)

    return render(request, 'drivers/driver-edit.html', {'form': form, 'driver': driver})


def driver_delete(request, pk):
    driver = get_object_or_404(Driver, pk=pk)

    if request.method == "POST":
        driver.delete()
        return redirect('drivers-list')

    return render(request, 'drivers/driver-delete.html', {'driver': driver})


def driver_standings(request):
    selected_team = request.GET.get('team', '')
    sort_by = request.GET.get('sort', 'championships')

    drivers = Driver.objects.select_related('team')

    if selected_team:
        drivers = drivers.filter(team_id=selected_team)

    allowed_sorts = {
        'championships': '-championships',
        'number': 'driver_number',
        'name': 'last_name',
    }
    drivers = drivers.order_by(allowed_sorts.get(sort_by, '-championships'), 'first_name')

    teams = Team.objects.all().order_by('name')

    context = {
        'drivers': drivers,
        'teams': teams,
        'selected_team': selected_team,
        'selected_sort': sort_by,
    }

    return render(request, 'drivers/driver-standings.html', context)