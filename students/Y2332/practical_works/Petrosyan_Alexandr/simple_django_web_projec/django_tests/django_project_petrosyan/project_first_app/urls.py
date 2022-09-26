from django.urls import path
from .views import *
urlpatterns = [

    # Cars ---------------------------------------------------------------------

    path('', show_home),

    path('owner/<int:owner_id>/', car_owner_detail),
    path('owner/list/', owners_list),
    path('owner/create/', create_owner),

    path('car/<int:pk>/', CarDetailView.as_view()),
    path('car/list/', CarsList.as_view()),
    path('car/create/', CreateCar.as_view()),
    path('car/<int:pk>/update/', UpdateCar.as_view()),
    path('car/<int:pk>/delete/', DeleteCar.as_view()),

    path('about/', show_about),

    # Examples -----------------------------------------------------------------

    # path('time/', show_time),
    # path('example_list/', list_view),
    # path('сvb_example_list/', ExampleList.as_view()),
    # path('publisher/<int:pk>/', PublisherRetrieveView.as_view()),
    # path('book/list/', BookListView.as_view()),
    #
    # path('example_create/', create_view),
    # path('cvb_example_create/', ExampleCreate.as_view(success_url="/сvb_example_list/")),
    # path('publisher/<int:pk>/update/', PublisherUpdateView.as_view()),
    # path('publisher/create/', PublisherCreateView.as_view()),
    # path('publisher/<int:pk>/delete/', PublisherDeleteView.as_view()),


]
