from django.db import models

# Create your models here.
class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    driver_number = models.PositiveIntegerField(unique=True)
    championships = models.PositiveIntegerField(default=0)
