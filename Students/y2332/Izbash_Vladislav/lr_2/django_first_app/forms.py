from django.forms import ModelForm
from .models import CarOwner


class CarOwnerForm(ModelForm):

    class Meta:
        model = CarOwner
        fields = [
            'first_name', 
            'last_name', 
            'birth_date', 
            'password',
            'nationality',
            'passport',
            'username'
        ]
