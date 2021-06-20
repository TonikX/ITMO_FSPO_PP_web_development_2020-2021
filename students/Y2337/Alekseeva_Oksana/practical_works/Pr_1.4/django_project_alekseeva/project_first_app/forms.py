from django import forms
from .models import *


# creating a form
class Car_ownerForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Car_owner

        # specify fields to be used
        fields = [
            "surname",
            "name",
            "date_of_birth",
        ]