# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Team
from .forms import TeamCreateForm


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