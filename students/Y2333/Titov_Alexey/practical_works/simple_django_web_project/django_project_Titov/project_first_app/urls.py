from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('owner/<int:owner_id>', views.owner),
    path('owner/create', views.owner_create),
    path('owner/all', views.owner_list),

    path('car/<int:pk>', views.CarDetail.as_view()),
    path('car/all', views.CarList.as_view()),
    path('car/create', views.CarCreate.as_view()),
    path('car/<int:pk>/edit', views.CarUpdate.as_view()),
    path('car/<int:pk>/delete', views.CarDelete.as_view()),
]
