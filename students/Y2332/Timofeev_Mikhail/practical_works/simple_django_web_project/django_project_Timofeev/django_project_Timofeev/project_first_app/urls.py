from django.urls import path
from .views import *
urlpatterns = [
    path('owner/<int:car_owner_id>/', detail),
    path('owners/', all_owners),
    path('add_owner', add_owner),
    path('cars/', CarsList.as_view()),
    path('car/<int:pk>/', CarView.as_view()),
    path('car/<int:pk>/update', CarUpdate.as_view()),
    path('car/create', CarCreate.as_view()),
    path('car/<int:pk>/delete', CarDelete.as_view()),
    path('example_list/', list_view),
    path('time/', time),
    path('сvb_example/', ExampleList.as_view()),
    path('publisher/<int:pk>/', PublisherRetrieveView.as_view()),
    path('book/list/', BookListView.as_view()),
    path('example_create', create_view),
    path('publisher/<int:pk>/update/', PublisherUpdateView.as_view()),
    path('cvb_example_create', ExampleCreate.as_view(success_url="/сvb_example/")),
    path('publisher/create/', PublisherCreateView.as_view()),
    path('publisher/<int:pk>/delete/', PublisherDeleteView.as_view()),
]
