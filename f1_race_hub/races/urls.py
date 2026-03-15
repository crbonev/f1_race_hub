from django.urls import path
from . import views

urlpatterns = [
    path('', views.races_list, name='races-list'),
    path('create/', views.race_create, name='race-create'),
    path('<int:pk>/', views.race_details, name='race-details'),
    ]