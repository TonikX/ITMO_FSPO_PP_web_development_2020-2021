from django.contrib import admin
from django.urls import path, include
from .views import redirect_blog
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', redirect_blog),
    path('admin/', admin.site.urls),
    path('', include('repairs_wagon_app.urls')),
]
