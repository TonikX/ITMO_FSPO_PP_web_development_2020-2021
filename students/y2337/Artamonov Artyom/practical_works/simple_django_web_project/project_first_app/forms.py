from django import forms
from .models import CarOwner, Car


# creating a form
class CarOwnerForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = CarOwner
  
        # specify fields to be used
        fields = [
            "firstname",
            "lastname",
            "cars",
            "date_of_birth",
        ]


# creating a form
class CarForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = Car
  
        # specify fields to be used
        fields = [
            "gov_number",
            "brand",
            "model",
            "color",
        ]
