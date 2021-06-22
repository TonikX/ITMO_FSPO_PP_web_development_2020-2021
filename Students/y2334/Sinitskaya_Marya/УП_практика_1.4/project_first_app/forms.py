from django import forms
# from .models import autoOwner
from .models import User


# creating a form
class ExampleForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = User

        # specify fields to be used
        fields = [
            "username",
            "birth_date",
            "passport",
            "address",
            "nationality"
        ]