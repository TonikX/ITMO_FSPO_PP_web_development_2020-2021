from django import forms
from .models import *
#from django.contrib.auth import get_user_model
#CarOwner = get_user_model


class OwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner

        fields = [
            "username",
            "first_name",
            "last_name",
            "birthday",
            "passport_id",
            "address",
            "nationality",
        ]
