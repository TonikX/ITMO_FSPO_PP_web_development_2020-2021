from django import forms
from .models import ExampleModel
from .models import CarOwner


# Cars -------------------------------------------------------------------------

class OwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = [
            "first_name",
            "last_name",
            "birth_date",
        ]

# Examples ---------------------------------------------------------------------


class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = [
            "title",
            "description",
        ]
