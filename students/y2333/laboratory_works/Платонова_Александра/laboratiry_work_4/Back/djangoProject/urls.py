"""djangoProject URL Configuration

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
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include, re_path

# vue_urls = [
#     path('', lambda request: HttpResponse(render(request, 'vue_index.html'))),
# ]
from rest_framework import routers

from check_in_app import views

# vue_urls = [
#   path('', views.frontend),
#   path('another-path/', views.frontend),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('check_in_app.urls')),
    path('auth/', include('djoser.urls')),
    # path('', include(vue_urls)),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
