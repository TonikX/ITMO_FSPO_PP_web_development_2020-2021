"""medicine_project URL Configuration

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
# from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from medicine_storage import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('api/users', views.UsersList.as_view(), name='users'),
    path('api/active-substances', views.ActiveSubstancesList.as_view(), name='active-substances'),
    path('api/manufactures', views.ManufacturersList.as_view(), name='manufactures'),
    path('api/items', views.ItemsList.as_view(), name='items'),
    path('api/units', views.UnitsList.as_view(), name='units'),
] + static('/', document_root='./dist/')
