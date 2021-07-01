from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from app import views


router = routers.DefaultRouter()
router.register(r'services', views.ServiceViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'doctor-services', views.DoctorServiceViewSet)
router.register(r'tickets', views.TicketViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]