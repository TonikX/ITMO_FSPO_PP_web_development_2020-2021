from django import forms
from .models import ExampleModel

from .models import Car
from .models import CarOwner

class CarForm(forms.ModelForm):


    class Meta:
        model = Car

        fields = [
           "gos_number",
            "mark",
            "model",
            "color",
        ]


class OwnerForm(forms.ModelForm):
    class Meta:

        model = CarOwner

        fields = [
        "last_name",
        "first_name",
        "bith_date",
    ]
