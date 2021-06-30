from django import forms
from .models import Owner


# creating a form
class ExampleForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Owner

        # specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "birth_date"
        ]