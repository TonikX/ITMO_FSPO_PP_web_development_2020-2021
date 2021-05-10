"""djangoRegistryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view

from registry.models import *
from registry.views import CardView


schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hardbeat34@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home', CardView.as_view()),
    path('doc/swagger', schema_view.as_view()),
    # url(r'^$', get_swagger_view(title='Pastebin API'))
    # path('doc/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

for model in [Building, Department, Worker, Management, Hall, Responsibility, Property, Unit, Consist, Revaluation]:
    name, root = model.__name__, model.__name__.lower()
    urlpatterns += [
        path(f'{root}/list', model.generate_list_view(title=f'{name} list', paginate_by=2)),
        path(f'{root}/<int:pk>', model.generate_detail_view(title=f'{name} details')),
        path(f'{root}/create', model.generate_create_view()),
        path(f'{root}/<int:pk>/delete', model.generate_delete_view()),
        path(f'{root}/search', model.generate_search_view(), name=f'search_results'),
    ]
