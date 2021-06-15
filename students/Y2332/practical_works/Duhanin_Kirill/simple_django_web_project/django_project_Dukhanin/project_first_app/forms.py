from django import forms
from .models import *


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner

        fields = [
            'first_name',
            'second_name',
            'birthdate',
            'passport_number',
            'address',
            'nationality',
            'password',
            'username'
        ]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car

        fields = [
            'state_number',
            'brand',
            'model',
            'color'
        ]
