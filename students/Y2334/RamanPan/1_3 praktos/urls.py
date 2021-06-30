"""blogfspo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django import VERSION
from django.core.exceptions import ViewDoesNotExist

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owner/<int:id>/', views.detail),
    path('list_view_car_owner/', views.list_view_car_owner),
    path('class_list_view_auto/', views.class_list_view_auto.as_view()),
    path('auto/<int:pk>/', views.auto_view.as_view()),
    path('ownership/', views.CarOwnersListView.as_view()),
    path('car_owner_view/', views.create_view),
    path('auto/<int:pk>/update', views.AutoUpdate.as_view()),
    path('auto/create', views.AutoCreate.as_view(success_url = '/class_list_view_auto/')),
    path('auto/<int:pk>/delete', views.AutoDelete.as_view())
]
