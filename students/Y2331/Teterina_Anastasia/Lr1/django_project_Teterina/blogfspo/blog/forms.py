from django import forms
from .models import *


# creating a form
class ExampleForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Owner

        # specify fields to be used
        fields = [
            "owner_id",
            "last_name",
            "name",
            "date_birth",
        ]
class Car_form(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Car

        # specify fields to be used
        fields = [
            "car_id",
            "gov_number",
            "brand",
            "model",
            "colour",
        ]

