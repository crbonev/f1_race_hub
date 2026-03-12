from django.db import models

from f1_race_hub.teams.models import Team


# Create your models here.
class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    driver_number = models.PositiveIntegerField(unique=True)
    championships = models.PositiveIntegerField(default=0)

    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='drivers',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'