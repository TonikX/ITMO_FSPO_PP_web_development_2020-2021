from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('books/', views.books, name='books'),
    path('create_book/', views.createBook, name="create_book"),
    path('update_book/<str:pk>/', views.updateBook, name="update_book"),
    path('delete_book/<str:pk>/', views.deleteBook, name="delete_book"),

    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
