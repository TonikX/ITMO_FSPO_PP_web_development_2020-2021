"""portfolio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from feedback.views import FeedbackViewSet, FeedbackAPIView, ServiceFeedbackAPIView, FeedbackDetailAPIView
from order.views import ServiceViewSet, OrderViewSet, OrderServiceAPIView, UsernameAPIView
from portfolio_project import settings
from projects.views import ProjectViewSet

router = SimpleRouter()

router.register(r'projects', ProjectViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'orders', OrderViewSet)
# router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    path('userorders/', OrderServiceAPIView.as_view()),
    path('username/', UsernameAPIView.as_view()),
    path('feedbacks/', FeedbackAPIView.as_view()),
    path('feedbacks/<int:service_id>/', ServiceFeedbackAPIView.as_view()),
    path('feedbacks/detail/<int:pk>/', FeedbackDetailAPIView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
