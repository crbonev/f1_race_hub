# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Team
from .forms import TeamCreateForm, TeamEditForm


def teams_list(request):
    teams = Team.objects.all()
    return render(request, 'teams/teams-list.html', {'teams': teams})


def team_details(request, pk):
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'teams/team-details.html', {'team': team})


def team_create(request):
    if request.method == "POST":
        form = TeamCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('teams-list')

    else:
        form = TeamCreateForm()

    return render(request, 'teams/team-create.html', {'form': form})


def team_edit(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == "POST":
        form = TeamEditForm(request.POST, instance=team)

        if form.is_valid():
            form.save()
            return redirect('team-details', pk)

    else:
        form = TeamEditForm(instance=team)

    return render(request, 'teams/team-edit.html', {'form': form, 'team': team})


def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == "POST":
        team.delete()
        return redirect('teams-list')

    return render(request, 'teams/team-delete.html', {'team': team})