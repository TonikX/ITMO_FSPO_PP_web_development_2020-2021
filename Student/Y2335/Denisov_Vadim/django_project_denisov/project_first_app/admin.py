from django.contrib import admin
from .models import Owner
from .models import Car
from .models import Ownership
from .models import License

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(License)
# Register your models here.
