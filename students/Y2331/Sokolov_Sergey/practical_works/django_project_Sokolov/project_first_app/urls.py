from django.urls import path
from .views import *


urlpatterns = [
    path('time/', cur_time),

    path('owner/', create_owner),
    path('owners/', owners_list),
    path('owners/<int:owner_id>/', owner_show),

    path('car/', CarCreate.as_view()),
    path('cars/', CarList.as_view()),
    path('cars/<int:pk>/', CarView.as_view()),
    path('cars/<int:pk>/update/', CarUpdate.as_view()),
    path('cars/<int:pk>/delete/', CarDelete.as_view()),
]

