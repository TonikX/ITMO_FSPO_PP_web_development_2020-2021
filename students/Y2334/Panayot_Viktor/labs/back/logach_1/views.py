from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
# Create your views here.

class LogikListView(generics.ListAPIView):
    queryset = Logik.objects.all()
    serializer_class = LogikSerializer

class LogikOneView(generics.RetrieveAPIView):
    queryset = Logik.objects.all()
    serializer_class = LogikSerializer

class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        queryset = Task.objects.all()

        ps = self.request.query_params
        theme = ps.get('theme', None)
        
        if theme:
            queryset = queryset.filter(theme=theme)
        return queryset

class TaskOneView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateTaskListView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UpdateTaskListView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    
class DeleteTaskListView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class LogikTaskListView(generics.ListAPIView):
    serializer_class = UpdateLogikTaskSerializer
    
    def get_queryset(self):
        queryset = LogikTask.objects.all()
        
        ps = self.request.query_params
        
        logik = ps.get('logik', None)
        task = ps.get('task', None)
        accept_date = ps.get('accept_date', None)
        solved = ps.get('solved', None)
        
        if logik:
            queryset = queryset.filter(logik=logik)
            
        if task:
            queryset = queryset.filter(task=task)
            
        if accept_date:
            queryset = queryset.filter(accept_date=accept_date)
            
        if solved:
            queryset = queryset.filter(solved=solved)
        return queryset

class LogikTaskOneView(generics.RetrieveAPIView):
    queryset = LogikTask.objects.all()
    serializer_class = LogikTaskSerializer

class DropLogikTask(generics.DestroyAPIView):
    queryset = LogikTask.objects.all()
    serializer_class = LogikTaskSerializer

class CreateLogikTaskListView(generics.CreateAPIView):
    queryset = LogikTask.objects.all()
    serializer_class = UpdateLogikTaskSerializer

class UpdateLogikTaskListView(generics.UpdateAPIView):
    queryset = LogikTask.objects.all()
    serializer_class = UpdateLogikTaskSerializer