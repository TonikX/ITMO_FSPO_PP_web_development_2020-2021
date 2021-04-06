from django import forms
from .models import Car_owner



class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = Car_owner
        fields = [
            "first_name",
            "last_name",
            "birthdate",
            "passport_number",
            "home_address",
            "nationality",
            "username",
            "password"
        ]
