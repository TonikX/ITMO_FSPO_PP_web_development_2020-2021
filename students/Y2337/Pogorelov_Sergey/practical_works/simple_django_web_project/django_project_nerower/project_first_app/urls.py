from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('home/', views.home),

    path('owner/list/', views.owner_list),
    path('owner/<int:owner_id>/', views.owner_info),
    
    path('car/list/', CarListView.as_view()),
    path('car/<int:pk>/', CarRetrieveView.as_view()),
    path('car/ownership/', CarOwnershipListView.as_view()),

    path('owner/create/', views.create_owner),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/create/', CarCreateView.as_view()),
                        #.as_view(success_url = '/car/list')
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
]
