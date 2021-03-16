from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('home/', views.home),
    path('owner/list/', views.owner_list),
    path('owner/<int:owner_id>/', views.owner_info),
    
    path('car/list/', CarListView.as_view()),
    path('car/<int:pk>/', CarRetrieveView.as_view()),
]
