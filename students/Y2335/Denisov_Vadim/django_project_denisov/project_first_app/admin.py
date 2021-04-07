from django.contrib import admin
from .models import User
from .models import Car
from .models import Ownership
from .models import License

admin.site.register(Car)
admin.site.register(License)
admin.site.register(Ownership)
admin.site.register(User)
