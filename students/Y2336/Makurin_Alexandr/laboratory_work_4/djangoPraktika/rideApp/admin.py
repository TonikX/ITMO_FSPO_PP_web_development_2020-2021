from django.contrib import admin
from .models import Ride, Playground, Usage

admin.site.register(Ride)
admin.site.register(Playground)
admin.site.register(Usage)

# Register your models here.
