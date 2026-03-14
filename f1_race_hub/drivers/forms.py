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

    def driver_number_validation(self):
        number = self.cleaned_data['driver_number']
        if number < 1 or number > 99:
            raise forms.ValidationError("Driver Number must be between 1 and 99")
        return number


class DriverEditForm(CreateDriverForm):
    class Meta(CreateDriverForm.Meta):
        exclude = ['driver_number']