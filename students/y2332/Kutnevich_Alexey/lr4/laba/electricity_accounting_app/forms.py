from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import *


class RenterForm(forms.ModelForm):
    class Meta:
        model = Renter
        fields = [
            "passport",
            "firstName",
            "surname",
            "patronymic",
            "privilege"
        ]


class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = [
            "district",
            "street"
        ]


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = [
            "idAdress",
            "buildingNumb",
            "building"
        ]


class InspectorForm(forms.ModelForm):

    class Meta:
        model = Inspector
        fields = [
            "servNumb",
            "first_name",
            "last_name",
            "patronymic",
            "phone",
        ]


class InspectorFormUpdate(forms.ModelForm):

    class Meta:
        model = Inspector
        fields = [
            "first_name",
            "last_name",
            "patronymic",
            "phone",
            "is_staff",
            "is_superuser"
        ]


class BypassForm(forms.ModelForm):
    class Meta:
        model = Bypass
        fields = [
            "inspectorServNumb",
            "status",
            "dateOfBypass",
            "flat",
            "comment"
        ]


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = [
            "flat",
            "flatType",
            "eStove",
            "peopleCount",
            "house",
            "renter"
        ]


class CreateInspectorForm(UserCreationForm):
    class Meta:
        username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
        password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        servNumb = forms.CharField(label='Service number', widget=forms.TextInput(attrs={'class': 'form-input'}))
        last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-input'}))
        first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'form-input'}))
        patronymic = forms.CharField(label='Patronymic', widget=forms.TextInput(attrs={'class': 'form-input'}))
        phone = forms.CharField(label='Phone number', widget=forms.TextInput(attrs={'class': 'form-input'}))
        model = Inspector
        fields = ('username', 'password1', 'password2', 'servNumb', 'last_name', 'first_name', 'patronymic', 'phone', 'is_staff', 'is_superuser')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
            'servNumb': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-input'})
        }


class RegisterInspectorForm(UserCreationForm):
    class Meta:
        username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
        password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        servNumb = forms.CharField(label='Service number', widget=forms.TextInput(attrs={'class': 'form-input'}))
        last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-input'}))
        first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'form-input'}))
        patronymic = forms.CharField(label='Patronymic', widget=forms.TextInput(attrs={'class': 'form-input'}))
        phone = forms.CharField(label='Phone number', widget=forms.TextInput(attrs={'class': 'form-input'}))
        model = Inspector
        fields = ('username', 'password1', 'password2', 'servNumb', 'last_name', 'first_name', 'patronymic', 'phone')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
            'servNumb': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'})
        }


class LoginInspectorForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'})),
    servNumb = forms.CharField(label='Service number', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
