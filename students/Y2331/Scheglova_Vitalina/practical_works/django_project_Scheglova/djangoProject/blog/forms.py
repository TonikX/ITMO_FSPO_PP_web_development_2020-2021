from django import forms
from .models import Plane_type, Client, Ticket_office


# class Planeform(forms.Form):
#     model_name = forms.CharField(max_length=20)
#     manufacturer = forms.CharField(max_length=20)
#     capacity = forms.IntegerField()

class PlaneForm(forms.ModelForm):
    class Meta:
        model = Plane_type
        fields = ['model_name', 'manufacturer', 'capacity']

class PlaneTypeForm(forms.ModelForm):
    class Meta:
        model = Plane_type
        fields = ['model_name', 'manufacturer', 'capacity']

class ClientsForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['FIO_client', 'passport_number', 'date_of_passport_start', 'registration_number', 'who_give_the_passport']

class Ticket_officeForm(forms.ModelForm):
    class Meta:
        model = Ticket_office
        fields = ['ticket_office_adress']