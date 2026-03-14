from django.urls import path
from . import views

urlpatterns = [
    path('', views.drivers_list, name='drivers-list'),
    path('create/', views.driver_create, name='driver-create'),
    path('<int:pk>/', views.driver_details, name='driver-details'),
    path('<int:pk>/edit/', views.driver_edit, name='driver-edit'),
    path('<int:pk>/delete/', views.driver_delete, name='driver-delete'),
]