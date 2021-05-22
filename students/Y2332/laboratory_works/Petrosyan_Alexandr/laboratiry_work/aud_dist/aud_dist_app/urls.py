from django.urls import path

from .views import ScheduleApiView

urlpatterns = [
    path('schedule/', ScheduleApiView.as_view())
]