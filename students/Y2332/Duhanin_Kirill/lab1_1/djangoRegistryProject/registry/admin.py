from django.contrib import admin
from .models import *


admin.site.register(CardModel)
# CardModel.objects.all().delete()

for model in [Building, Department, Worker, Management, Hall, Responsibility, Property, Unit, Consist, Revaluation]:
    admin.site.register(model.model)

