from django.contrib import admin
from django.contrib.admin import ModelAdmin

from feedback.models import Feedback


@admin.register(Feedback)
class UserAdmin(ModelAdmin):
    pass
