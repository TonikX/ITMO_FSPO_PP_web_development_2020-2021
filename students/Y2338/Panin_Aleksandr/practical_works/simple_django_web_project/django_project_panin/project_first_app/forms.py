from django import forms
from .models import CarOwner


class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = [
            "username",
            "password",
            "surname",
            "name",
            "birthday",
            "passport",
            "address",
            "nationality"
        ]