from django import forms
from .models import *


# creating a form
class CreateForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = CarOwner

        # specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "date_birth",
        ]


class CarForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Car

        # specify fields to be used
        fields = [
            "mark",
            "model",
            "color",
            "number",
        ]
