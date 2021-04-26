from django.contrib import admin  # импорт данных из таблицы

from .models import Owner, Drivers_license, Car, Possession  # импорт каких таблиц

admin.site.register(Owner)  # импорт  овнера
admin.site.register(Drivers_license)  # импорт  водительских прав
admin.site.register(Car)  # импорт  машины
admin.site.register(Possession)  # импорт владельца

# Создание админ панели
from django.contrib import admin
from .models import ExampleModel

admin.site.register(ExampleModel)
