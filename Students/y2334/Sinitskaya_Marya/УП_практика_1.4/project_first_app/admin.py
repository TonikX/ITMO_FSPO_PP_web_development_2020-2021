from django.contrib import admin

# Register your models here.
from .models import Owner, User

admin.site.register(Owner)

from .models import Car
admin.site.register(Car)

from .models import Ownership
admin.site.register(Ownership)

from .models import DriverLicense
admin.site.register(DriverLicense)

from .models import AbstractUser
admin.site.register(User)