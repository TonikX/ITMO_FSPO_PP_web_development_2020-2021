from django.contrib import admin

from .models import Owner, License, Auto, Ownership, ExampleModel

admin.site.register(Owner)
admin.site.register(License)
admin.site.register(Auto)
admin.site.register(Ownership)
admin.site.register(ExampleModel)
# Register your models here.
