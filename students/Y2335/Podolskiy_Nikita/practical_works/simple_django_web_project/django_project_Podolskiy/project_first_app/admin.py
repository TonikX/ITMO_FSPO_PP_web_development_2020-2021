from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User

#from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Owner
from .models import Car
from .models import Ownership
from .models import License

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(License)