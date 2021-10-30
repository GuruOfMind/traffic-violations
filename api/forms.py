from django import forms
from django.forms import ModelForm

from .models import Vehicle

class DateInput(forms.DateInput):
    input_type = 'date'

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['plugged_number', 'driver', 'type', 'category ', 'production_date', 'registration_date']
        widgets = {
         'production_date' : DateInput(),
         'registration_date' : DateInput()    
        }

