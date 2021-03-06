from django.urls import path
from .views import *
urlpatterns = [

    # Cars ---------------------------------------------------------------------

    path('owner/<int:owner_id>/', car_owner_detail),
    path('owners_list/', owners_list),
    path('car/<int:pk>/', CarDetailView.as_view()),

    # TODO: Cars list 

    # Examples -----------------------------------------------------------------

    path('time/', show_time),
    path('example_list/', list_view),
    path('сvb_example_list/', ExampleList.as_view()),
    path('publisher/<int:pk>/', PublisherRetrieveView.as_view()),
    path('book/list/', BookListView.as_view()),
]
