from django import forms
from .models import *


class OwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner

        fields = [
            "first_name",
            "last_name",
            "birthday",
            "cars",
        ]
