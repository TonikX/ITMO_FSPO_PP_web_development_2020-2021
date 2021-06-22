from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RideViewSet, PlaygroundViewSet, UsageViewSet

app_name = "rideApp"
# app_name will help us do a reverse look-up latter.
router = DefaultRouter()
router.register(r'rides', RideViewSet)
router.register(r'playgrounds', PlaygroundViewSet)
router.register(r'usages', UsageViewSet)
urlpatterns = [
    path('', include(router.urls)),
]