from django.urls import path
from . import views
urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('owner_list/', views.list_view),
    path('сvb_example/', views.ExampleList.as_view()),
    path('car/<int:pk>/', views.CarRetrieveView.as_view()),
    path('car/list/', views.CarListView.as_view()),
    path('example_create', views.create_view),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('cvb_example_create', views.CarCreate.as_view(success_url="/сvb_example/")),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view()),
    ##path('car/<int:pk>/update/', views.car_form),
]