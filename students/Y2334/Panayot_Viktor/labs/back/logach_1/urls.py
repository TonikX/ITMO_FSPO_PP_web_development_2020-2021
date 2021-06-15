# from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('logik/all', LogikListView.as_view()),
    path('logik/<int:pk>', LogikOneView.as_view()),
    path('task/all', TaskListView.as_view()),
    path('task/<int:pk>', TaskOneView.as_view()),
    path('task/update/<int:pk>', UpdateTaskListView.as_view()),
    path('task/new', CreateTaskListView.as_view()),
    path('usertask/all', LogikTaskListView.as_view()),
    path('usertask/<int:pk>', LogikTaskOneView.as_view()),
    path('usertask/update/<int:pk>', UpdateLogikTaskListView.as_view()),
    path('usertask/drop/<int:pk>', DropLogikTask.as_view()),
    path('usertask/new', CreateLogikTaskListView.as_view()),
]