from django.urls import path
from .views import *
urlpatterns = [
    path('owner/<int:owner_id>', owner_detail),
    path('car/<int:pk>', CarRetrieveView.as_view()),

    path('owner/list', list_owners),
    path('car/list', CarListView.as_view()),

    path('owner/create', create_owner),
    path('car/create', CarCreateView.as_view()),

    path('car/<int:pk>/delete', CarDeleteView.as_view()),
    path('car/<int:pk>/update', CarUpdateView.as_view())
]
