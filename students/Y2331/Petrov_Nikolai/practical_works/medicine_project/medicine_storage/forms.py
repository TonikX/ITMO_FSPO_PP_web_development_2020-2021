from django.forms import ModelForm
from medicine_storage import models
from django.utils.translation import gettext_lazy as _


class ActiveSubstanceForm(ModelForm):
    class Meta:
        model = models.ActiveSubstance
        fields = ['name']
        labels = {
            'name': _('Название')
        }


class ManufacturerForm(ModelForm):
    class Meta:
        model = models.Manufacturer
        fields = ['name', 'country']
        labels = {
            'name': _('Название'),
            'country': _('Страна')
        }


class ItemForm(ModelForm):
    class Meta:
        model = models.Item
        fields = ['name', 'active_substance', 'packaging', 'manufacturer']
        labels = {
            'name': _('Название'),
            'active_substance': _('Действующее вещество'),
            'packaging': _('Тип упаковки'),
            'manufacturer': _('Производитель')
        }


class UnitForm(ModelForm):
    class Meta:
        model = models.Unit
        # fields = ['item', 'amount', 'product_date', 'open_date', 'user']
        fields = ['item', 'amount', 'product_date', 'user']
        labels = {
            'item': _('Название'),
            'amount': _('Количество'),
            'product_date': _('Дата производства'),
            # 'open_date': _('Дата вскрытия упаковки')
        }
