from django.db import models
from f1_race_hub.drivers.models import Driver
# Create your models here.

class Race(models.Model):
    name = models.CharField(max_length=100)
    circuit = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    race_date = models.DateField()
    season = models.PositiveIntegerField()