"""project_first_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    
    path('owner/list', views.OwnerListView.as_view()),
    path('owner/create', views.OwnerCreateView.as_view()),
    path('owner/<int:pk>/update', views.OwnerUpdateView.as_view()),
    path('owner/<int:pk>/delete', views.OwnerDeleteView.as_view()),
    path('owner/<int:pk>', views.OwnerDetailView.as_view()),

    path('license/list', views.DriversLicenseListView.as_view()),
    path('license/create', views.DriversLicenseCreateView.as_view()),
    path('license/<int:pk>/update', views.DriversLicenseUpdateView.as_view()),
    path('license/<int:pk>/delete', views.DriversLicenseDeleteView.as_view()),
    path('license/<int:pk>', views.DriversLicenseDetailView.as_view()),

    path('auto/list', views.AutoListView.as_view()),
    path('auto/create', views.AutoCreateView.as_view()),
    path('auto/<int:pk>/update', views.AutoUpdateView.as_view()),
    path('auto/<int:pk>/delete', views.AutoDeleteView.as_view()),
    path('auto/<int:pk>', views.AutoDetailView.as_view()),

    path('auto_owner/list', views.AutoOwnerListView.as_view()),
    path('auto_owner/create', views.AutoOwnerCreateView.as_view()),
    path('auto_owner/<int:pk>/update', views.AutoOwnerUpdateView.as_view()),
    path('auto_owner/<int:pk>/delete', views.AutoOwnerDeleteView.as_view()),
    path('auto_owner/<int:pk>', views.AutoOwnerDetailView.as_view()),
]
