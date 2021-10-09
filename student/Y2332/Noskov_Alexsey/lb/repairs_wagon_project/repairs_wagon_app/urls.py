from django.urls import path
from django.conf.urls import url
from django.views.generic import ListView
from . import views
from . import models
urlpatterns = [
    path('worker/<int:pk>/', views.Worker_detail.as_view(), name="worker_d"),
    path('worker/list/', views.Worker_List.as_view(), name='worker_l'),
    path('worker/<int:pk>/update/', views.WorkerUpdateView.as_view(), name="worker_u"),
    path('worker/add/', views.WorkerCreate.as_view()),
    path('worker/<int:pk>/delete/', views.WorkerDelete.as_view(), name="worker_del"),
    path('wagon/<int:pk>/', views.Wagon_detail.as_view(), name="wagon_d"),
    path('wagon/list/', views.Wagon_List.as_view(), name='wagon_l'),
    path('wagon/<int:pk>/update/', views.WagonUpdateView.as_view(), name="wagon_u"),
    path('wagon/add/', views.WagonCreate.as_view()),
    path('wagon/<int:pk>/delete/', views.WagonDelete.as_view(), name="wagon_del"),
    path('repair/<int:pk>/', views.Repair_detail.as_view(), name="repair_d"),
    path('repair/list/', views.Repair_List.as_view(), name='repair_l'),
    path('repair/<int:pk>/update/', views.RepairUpdateView.as_view(), name="repair_u"),
    path('repair/add/', views.RepairCreate.as_view()),
    path('repair/<int:pk>/delete/', views.RepairDelete.as_view(), name="repair_del"),
    path('menu_reliz/', views.Menu_reliz.as_view()),
]
