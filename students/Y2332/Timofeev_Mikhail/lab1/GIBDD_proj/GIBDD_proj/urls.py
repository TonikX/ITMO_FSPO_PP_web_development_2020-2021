from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from GIBDD_app.models import *
from GIBDD_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda req: redirect('/home')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

router = DefaultRouter()

router.register('bodies', BodyViewSet, basename='body')
router.register('engines', EngineViewSet, basename='engine')
router.register('models', CarModelViewSet, basename='model')
router.register('legal_owners', LegalOwnerViewSet, basename='legal_owner')
router.register('physical_owners', PhysicalOwnerViewSet, basename='physical_owner')
router.register('cars', CarViewSet, basename='car')
router.register('drive_away_info_list', DriveAwayInfoViewSet, basename='drive_away_info')
router.register('inspectors', InspectorViewSet, basename='inspector')
router.register('watch_info_list', WatchInfoViewSet, basename='watch_info')

urlpatterns += router.urls
