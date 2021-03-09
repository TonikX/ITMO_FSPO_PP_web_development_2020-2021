from django import forms
from .models import ExampleModel
from .models import CarOwner


# creating a form
class ExampleForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = ExampleModel

        # specify fields to be used
        fields = [
            "title",
            "description",
        ]


class OwnerForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = CarOwner

        # specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "birth_date",
            "cars"
        ]
