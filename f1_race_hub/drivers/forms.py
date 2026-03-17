from django import forms
from .models import Driver

class CreateDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = (
            'first_name',
            'last_name',
            'nationality',
            'driver_number',
            'championships',
            'team',
        )

        labels = {
            'driver_number':'Driver Number',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'Max'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Verstappen'}),
        }

    def clean_driver_number(self):
        number = self.cleaned_data['driver_number']
        if number < 1 or number > 99:
            raise forms.ValidationError("Driver Number must be between 1 and 99")
        return number


class DriverEditForm(CreateDriverForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["first_name"].disabled = True
        self.fields["last_name"].disabled = True

    def clean_first_name(self):
        if self.instance and self.instance.pk:
            return self.instance.first_name
        return super().clean().get("first_name")

    def clean_last_name(self):
        if self.instance and self.instance.pk:
            return self.instance.last_name
        return super().clean().get("last_name")