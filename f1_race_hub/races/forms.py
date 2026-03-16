from django import forms
from .models import Race, RaceResult


class RaceCreateForm(forms.ModelForm):
    class Meta:
        model = Race
        exclude = ['drivers']
        widgets = {
            'race_date': forms.DateInput(attrs={'type': 'date'}),
        }


class RaceResultForm(forms.ModelForm):
    class Meta:
        model = RaceResult
        fields = [
            'driver',
            'position',
            'points',
            'fastest_lap',
        ]