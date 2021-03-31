from django.urls import path 
from . import views

urlpatterns = [
    path('owner/<gov_number>', views.owners_info),
    path('owner/create', views.create_view, name='create_owner'),
    path('car/', views.CarListView.as_view()),
    path('car/create', views.create_view, name='create_car'),
    path('car/update/<int:pk>', views.CarUpdateView.as_view(), name='update_car'),
    path('car/delete/<int:pk>', views.CarDeleteView.as_view(), name='delete_car'),
]
