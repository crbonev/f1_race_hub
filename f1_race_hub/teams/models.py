from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    founded = models.PositiveIntegerField()
    team_principal = models.CharField(max_length=100)
    championships = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
