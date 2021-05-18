from django import forms
from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('representative_full_name',
                  'supervisor_full_name',
                  'customer_telephone',
                  'customer_account_number',
                  'customer_type',
                  'customer_inn',
                  'customer_address',
                  'customer_distinct')
        widgets = {
            'representative_full_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'ФИО клиента'}),
            'supervisor_full_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'ФИО начальника'}),
            'customer_telephone': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Телефон клиента'}),
            'customer_account_number': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Номер в банке'}),
            'customer_type': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Тип клиента'}),
            'customer_inn': forms.TextInput(attrs={'class': 'input', 'placeholder': 'ИНН клиента'}),
            'customer_address': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Адрес клиента'}),
            'customer_distinct': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Район клиента'}),
        }


class ModelForm(forms.ModelForm):
    class Meta:
        model = ModelTechnique
        fields = ('brand_technique',
                  'type_technique',
                  'manufacturer_technique')

        widgets = {
            'brand_technique': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Бренд техники'}),
            'type_technique': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Тип техники'}),
            'manufacturer_technique': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Производитель техники'}),
        }


class TechniqueForm(forms.ModelForm):
    class Meta:
        model = Technique
        fields = ('model_technique',
                  'customer',
                  'date_create',
                  'date_end_guarantee')
        widgets = {
            'model_technique': forms.Select(attrs={'class': 'input', 'placeholder': 'Модель техники'}),
            'customer': forms.Select(attrs={'class': 'input', 'placeholder': 'Клиент'}),
            'date_create': forms.DateInput(attrs={'class': 'input', 'type': 'date', 'placeholder': 'Дата создания'}),
            'date_end_guarantee': forms.DateInput(attrs={'class': 'input', 'type': 'date', 'placeholder': 'Дата конца гарантии'})
        }


class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ('master_full_name',
                  'insurance_number',
                  'master_phone',
                  'master_passport',
                  'master_qualification',
                  'work_experience',
                  'sum_amount_fine')
        widgets = {
            'master_full_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'ФИО мастера'}),
            'insurance_number': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Номер страховки'}),
            'master_phone': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Телефон мастера'}),
            'master_passport': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Номер паспорта'}),
            'master_qualification': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Квалификация мастера'}),
            'work_experience': forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Опыт работы'}),
            'sum_amount_fine': forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Сумма штрафов'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('technique',
                  'master',
                  'price_list',
                  'status_execution',
                  'status_guilt',
                  'note')
        widgets = {
            'technique': forms.Select(attrs={'class': 'input', 'placeholder': 'Техника'}),
            'master': forms.Select(attrs={'class': 'input', 'placeholder': 'Мастер'}),
            'price_list': forms.Select(attrs={'class': 'input', 'placeholder': 'Цена'}),
            'status_execution': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Статус выполнения'}),
            'status_guilt': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Статус виновности'}),
            'note': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Примечание'}),
        }


class PriceListForm(forms.ModelForm):
    class Meta:
        model = PriceList
        fields = (
            'name_service',
            'price'
        )
        widgets = {
            'name_service': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Название услуги'}),
            'price': forms.NumberInput(attrs={'class': 'input', 'placeholder': 'цена'}),
        }
