from django.contrib import admin

# Register your models here.


from .models import Car
from .models import CarOwner
from .models import Own
from .models import Doc
from .models import ExampleModel
from .models import Publisher

admin.site.register(Car)
admin.site.register(CarOwner)
admin.site.register(Own)
admin.site.register(Doc)
admin.site.register(ExampleModel)
admin.site.register(Publisher)
