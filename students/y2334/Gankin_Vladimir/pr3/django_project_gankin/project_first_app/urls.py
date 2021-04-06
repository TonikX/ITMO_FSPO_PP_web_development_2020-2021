from django.urls import path
from . import views
# from .views import time
# from .views import list_view_auto_owner
# from .views import AutoList
# from .views import AutoRetrieveView
# from .views import create_view
# from .views import AutoUpdateView
# from .views import AutoCreate
# from .views import AutoDeleteView
from .views import *
urlpatterns = [
    path('owner/<int:owner_id>', views.owner),
    path('auto/<int:auto_id>', views.auto),
    path('time/', time),
    path('list_view_auto_owner', list_view_auto_owner),
    path('auto_list', AutoList.as_view()),
    path('auto_detail/<int:pk>', AutoRetrieveView.as_view()),
    path('auto/list/', AutoListView.as_view()),
    path('auto_owner_create', create_view),
    path('auto/<int:pk>/update/', AutoUpdateView.as_view()),
    path('auto/create', AutoCreate.as_view()),
    path('auto/<int:pk>/delete/', AutoDeleteView.as_view()),
]
