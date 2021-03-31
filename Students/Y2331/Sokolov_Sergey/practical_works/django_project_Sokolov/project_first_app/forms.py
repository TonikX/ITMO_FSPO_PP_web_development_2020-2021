from django import forms
from .models import CarOwner


class OwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ['username', 'surname','passport_number', 'home_address', 'nationality', 'password']
