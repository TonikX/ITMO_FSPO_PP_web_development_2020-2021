from django.contrib import admin

from django.contrib import admin
from .models import Owner
from .models import Car
from .models import Document
from .models import Ownership

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Document)
admin.site.register(Ownership)
