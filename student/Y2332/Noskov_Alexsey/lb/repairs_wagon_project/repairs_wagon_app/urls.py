from django.urls import path
from django.conf.urls import url
from django.views.generic import ListView
from . import views
from . import models
urlpatterns = [
    path('worker/<int:pk>/', views.Worker_detail.as_view()),
    path('worker/list/', views.Worker_List.as_view()),
    path('worker/<int:pk>/update/', views.WorkerUpdateView.as_view()),
    path('worker/add/', views.WorkerCreate.as_view()),
    path('worker/<int:pk>/delete/', views.WorkerDelete.as_view()),
    path('wagon/<int:pk>/', views.Wagon_detail.as_view()),
    path('wagon/list/', views.Wagon_List.as_view()),
    path('wagon/<int:pk>/update/', views.WagonUpdateView.as_view()),
    path('wagon/add/', views.WagonCreate.as_view()),
    path('wagon/<int:pk>/delete/', views.WagonDelete.as_view()),
    path('repair/<int:pk>/', views.Repair_detail.as_view()),
    path('repair/list/', views.Repair_List.as_view()),
    path('repair/<int:pk>/update/', views.RepairUpdateView.as_view()),
    path('repair/add/', views.RepairCreate.as_view()),
    path('repair/<int:pk>/delete/', views.RepairDelete.as_view()),
    path('menu/', views.Menu.as_view()),
    url(r'^$',
        ListView.as_view(
            template_name='worker_list.html',
            queryset=models.Worker.objects.filter(tab_number__isnull=True).order_by('-tab_number'),
            paginate_by=1
        ),
        name='index'),

]
