from django import forms
from .models import CarOwner,Car

class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = [
            "first_name",
            "last_name",
            "birth_date",
        ]

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "number",
            "brand",
            "model",
            "color"
        ]
