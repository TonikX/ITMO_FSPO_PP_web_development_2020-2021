from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views 

urlpatterns = [
    path('', views.index),
    path('accounts/', include('django.contrib.auth.urls'), {'next_page': '/'}),
    path('books/', views.books),
    path('articles/', views.articles),
    path('writer/<int:pk>/', views.writer.as_view()),
    path('read_one_review/<int:pk>/', views.read_one_review.as_view()),
    path('discussion/<int:pk>/', views.discussion.as_view()),
    path('read_book/<int:pk>/', views.read_book.as_view()),
    path('read_article/<int:pk>/', views.read_article.as_view()),
    path('admin_dev/', views.admin_dev),
    path('password_recovery/', views.password_recovery),
    path('profile/', views.profile),
    path('profile_edit/', views.profile_edit),
    path('create_author/', views.create_author),
    path('article_confirmation/', views.article_confirmation),
    path('admin_create_composition/', views.admin_create_composition),
    path('confirmation_works/', views.confirmation_works),
    path('creat_composition/', views.creat_composition),
    path('create_article/', views.create_article),
    path('create_discussion/', views.create_discussion),
    path('create_rewies/', views.create_rewies),
    path('read_one_book/<int:pk>/', views.read_one_book.as_view()),
]
