from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Owner
from .models import Car
from .models import Ownership
from .models import License

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(License)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('id', 'is_staff', 'is_active',)
    list_filter = ('id', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('id', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('id',)
    ordering = ('id',)


admin.site.register(User, CustomUserAdmin)
