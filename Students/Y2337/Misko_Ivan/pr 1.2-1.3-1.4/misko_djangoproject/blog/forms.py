from django import forms
from .models import Owner, Car


# creating a form
class OwnerForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Owner

        # specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "birth_date",
            "passport_number",
            "home_address",
            "nationality",
        ]

class CarForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Car

        # specify fields to be used
        fields = [
            "state_number",
            "brand",
            "model",
            "color",
        ]