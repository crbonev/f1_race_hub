from django import forms
from .models import Team


class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Red Bull Racing'}),
            "team_principal": forms.TextInput(attrs={'placeholder': 'Christian Horner'}),
        }

    def clean_founded(self):
        year = self.cleaned_data['founded']

        if year < 1950:
            raise forms.ValidationError("F1 teams must be founded after 1950.")

        return year