from django import forms
from .models import *


# creating a form
class Owner_form(forms.ModelForm):
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