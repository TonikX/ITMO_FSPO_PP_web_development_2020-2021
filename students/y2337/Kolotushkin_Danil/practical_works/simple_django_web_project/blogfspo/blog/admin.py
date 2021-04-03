from django.contrib import admin
from .models import car
from .models import owner
from .models import card
from .models import owning

# Register your models here.
admin.site.register(car)
admin.site.register(owner)
admin.site.register(card)
admin.site.register(owning)
