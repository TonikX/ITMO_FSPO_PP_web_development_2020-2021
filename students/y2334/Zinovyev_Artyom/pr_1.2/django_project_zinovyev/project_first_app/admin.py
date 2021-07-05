from django.contrib import admin
from .models import AutoOwner, Auto, Owning, Paper

# Register your models here.
admin.site.register(AutoOwner)
admin.site.register(Auto)
admin.site.register(Owning)
admin.site.register(Paper)
