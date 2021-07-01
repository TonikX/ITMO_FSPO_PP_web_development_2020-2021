from django.contrib import admin

from .models import Owner

from .models import License

from .models import Auto

from .models import AutoOwner


admin.site.register(Owner)
admin.site.register(License)
admin.site.register(Auto)
admin.site.register(AutoOwner)
# Register your models here.
