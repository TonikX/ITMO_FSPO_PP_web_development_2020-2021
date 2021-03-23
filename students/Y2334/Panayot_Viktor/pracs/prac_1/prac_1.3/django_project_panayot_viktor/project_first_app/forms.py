from django import forms
from .models import car_owner

class CarForm(forms.ModelForm):
  
    class Meta:
        model = car_owner
  
        fields = [
            "Surname",
            "Name",
            "Date_of_Birth"
        ]