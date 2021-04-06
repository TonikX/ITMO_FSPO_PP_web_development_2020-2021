from django.contrib import admin

from .models import Car
from .models import CarOwner
from .models import Ownership
from .models import DriverLicense
# from .models import ExampleModel
# from .models import Publisher
# from .models import Book

admin.site.register(Car)
admin.site.register(CarOwner)
admin.site.register(Ownership)
admin.site.register(DriverLicense)
# admin.site.register(ExampleModel)
# admin.site.register(Publisher)
# admin.site.register(Book)
