from django import forms
from .models import CarOwner, Car


class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner

        fields = [
            "first_name",
            "second_name",
            "birth_date",
        ]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car

        fields = [
            "state_number",
            "brand",
            "model",
            "color",
        ]
