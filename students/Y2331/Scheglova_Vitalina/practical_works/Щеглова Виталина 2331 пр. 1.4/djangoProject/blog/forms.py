from django import forms  # импорт форм, чтобы была возможность их создавать
from .models import Owner  # импорт класса овнер, чтобы использовать его в дальнейших формах
from .models import Car  # импорт класса кар, чтобы использовать его в дальнейших формах


# Формы Django удобны тем, что мы можем создать новую форму с нуля или воспользоваться ModelForm для сохранения содержимого формы в модель.

# creating a form
class Owner_f(forms.ModelForm):  # напоминаем, что эта форма относится к ModelForm
    # Создаем класс мета
    class Meta:
        # сообщаем, какую модель мы будет использовать в дальнейшем
        model = Owner

        # поля, которые будут использованы в форме
        fields = [
            'username',
            'password',
            'last_name',
            'name',
            'birth_date',
            'address',
            'passport_number',
            'nationality',
        ]


class Car_f(forms.ModelForm):  # напоминаем, что эта форма относится к ModelForm
    # Создаем класс мета
    class Meta:
        # сообщаем, какую модель мы будет использовать в дальнейшем
        model = Car

        # поля, которые будут использованы в форме
        fields = [
            "Brand",
            "State_number",
            "Model",
            "Color",
        ]
