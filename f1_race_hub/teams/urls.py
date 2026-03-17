from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams_list, name='teams-list'),
    path('create/', views.team_create, name='team-create'),
    path('<int:pk>/', views.team_details, name='team-details'),
    path('<int:pk>/edit/', views.team_edit, name='team-edit'),
    path('<int:pk>/delete/', views.team_delete, name='team-delete'),
]