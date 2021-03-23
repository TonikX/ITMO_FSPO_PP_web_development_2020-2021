from django import forms

from project_first_app.models import CarOwner, Car


class OwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = [
            "last_name",
            "first_name",
            "birth_date",
        ]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "gos_number",
            "mark",
            "model",
            "color",
        ]

