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
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import ListView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view

from generator import generate_docs
from registry.models import *
from registry.views import CardView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home', CardView.as_view()),
    path('', lambda req: redirect('/home')),
]

for model in [Building, Department, Worker, Management, Hall, Responsibility, Property, Unit, Consist, Revaluation]:
    name, root = model.__name__, model.__name__.lower()
    urlpatterns += [
        path(*model.generate_list_view(title=f'{name} list', paginate_by=2)),
        path(*model.generate_detail_view()),
        path(*model.generate_create_view()),
        path(*model.generate_delete_view()),
        # path(*model.generate_search_view(), name='search_results'),
        path(*model.generate_update_view())
    ]
# generate_docs([Building, Department, Worker, Management, Hall, Responsibility, Property, Unit, Consist, Revaluation])