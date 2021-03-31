from django.contrib import admin

from .models import carOwner
from .models import car
from .models import licence
from .models import owning

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(carOwner,AuthorAdmin)
admin.site.register(car,AuthorAdmin)
admin.site.register(licence,AuthorAdmin)
admin.site.register(owning,AuthorAdmin)
# Register your models here.
