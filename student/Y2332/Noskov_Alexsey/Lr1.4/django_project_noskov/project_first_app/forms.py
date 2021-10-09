from django import forms
from .models import User, Car

class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "birth_date",
            "passport_number",
            "home_address",
            "nationality"
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
