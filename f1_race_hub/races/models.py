from django.db import models
from f1_race_hub.drivers.models import Driver
# Create your models here.

class Race(models.Model):
    name = models.CharField(max_length=100)
    circuit = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    race_date = models.DateField()
    season = models.PositiveIntegerField()

    drivers = models.ManyToManyField(Driver, through='RaceResult')

    def __str__(self):
        return f'{self.name} {self.season}'

class RaceResult(models.Model):
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE
    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE
    )

    position = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    fastest_lap = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.race} | {self.driver} | {self.position} | {self.points}'

class Meta:
    ordering = ['position']