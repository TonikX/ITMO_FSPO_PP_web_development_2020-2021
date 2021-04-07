from django import forms
from .models import *


# creating a form
class User_form(forms.ModelForm):
    # create meta class
    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "birthdate",
            "pass_num",
            "address",
            "nationality",
        ]