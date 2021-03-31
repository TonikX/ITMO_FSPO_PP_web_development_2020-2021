from django import forms
from .models import Car_owner
from .models import Car
from .models import Driver_license
from .models import Ownership


class Owner_form(forms.ModelForm):
    class Meta:
        model = Car_owner
        fields = [
            "surname",
            "name",
            "date_birth",
        ]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "license_number",
            "brand",
            "car_model",
            "color",
        ]
