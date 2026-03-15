from django.shortcuts import render, redirect, get_object_or_404
from .models import Driver
from .forms import CreateDriverForm, DriverEditForm


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