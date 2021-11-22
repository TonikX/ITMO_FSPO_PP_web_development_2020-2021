from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema = get_schema_view(
    openapi.Info(
        title='Elibary API',
        default_version='V1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', lambda _: redirect('static/elibrary/index.html')),
    path('admin/', admin.site.urls),
    path('api/', include('elibrary.urls')),
    path('api/docs/', schema.with_ui('swagger', cache_timeout=0), name='swagger'),
]
