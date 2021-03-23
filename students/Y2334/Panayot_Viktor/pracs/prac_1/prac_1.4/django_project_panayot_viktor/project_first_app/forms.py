from django import forms
from .models import CarOwner

class CarForm(forms.ModelForm):
    
    class Meta:
        model = CarOwner
        fields = [
            "email",
            "username",
            "password",
            "last_login",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "Surname",
            "Name",
            "Date_of_Birth",
            "passport_number",
            "home_adress",
            "citizenship"
        ]