from django.urls import path
from .views import *

urlpatterns = [
    path('owner_id/<int:owner_id>/', detail),
    path('owner/list/', owner_list),
    path('owner/<int:pk>/', CarOwner_id.as_view()),
    path('owner/create/', create_owner),
    #path('car/list/', Car_list.as_view()),
    path('car/list/', CarList.as_view()),
    path('car/<int:pk>/', Car_id.as_view()),
    path('car/<int:pk>/update/', CarUpdate.as_view()),
    path('car/create/', CarCreate.as_view()),
    path('car/<int:pk>/delete/', CarDelete.as_view()),
]
