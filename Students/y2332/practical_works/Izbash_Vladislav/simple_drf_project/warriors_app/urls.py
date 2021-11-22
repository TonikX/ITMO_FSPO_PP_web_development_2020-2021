from django.urls import path
from .views import *


app_name = 'warriors_app'


urlpatterns = [
     path('skills/list', SkillList.as_view()),
     path('skills/create', SkillCreate.as_view()),
     path('warriors/profs', WarriorProfList.as_view()),
     path('warriors/skills', WarriorSkillsList.as_view()),
     path('warriors/<int:pk>', WarriorGet.as_view()),
     path('warriors/<int:pk>/delete', WarriorDelete.as_view()),
     path('warriors/<int:pk>/update', WarriorUpdate.as_view()),
]
