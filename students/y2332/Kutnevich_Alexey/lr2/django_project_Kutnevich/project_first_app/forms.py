from django import forms
from .models import *


class CarForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = Car

        # specify fields to be used
        fields = [
            "number",
            "stump",
            "model",
            "color"
        ]


class CreateOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner

        fields = [
            'Second_name',
            'First_name',
            'Birth',
            'cars'
        ]


class UpdateOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner

        fields = [
            'Second_name',
            'First_name',
            'Birth',
            'cars'
        ]


class OwnerDelete(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = []