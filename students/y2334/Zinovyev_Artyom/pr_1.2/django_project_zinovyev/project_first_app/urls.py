from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.owner),
    path('owners', views.OwnersList.as_view()),
    path('addOwner', views.addOwner.as_view(success_url='/owners')),
    path('autos', views.AutosList.as_view()),
    path('auto/<int:pk>/', views.AutoRetrieve.as_view()),
    path('addAuto', views.AddAuto.as_view(success_url='/autos')),
    path('removeAuto/<int:pk>', views.RemoveAuto.as_view())
]

