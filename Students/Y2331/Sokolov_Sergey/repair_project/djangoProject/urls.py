from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from repair_technique import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('orders/create', views.OrderCreate.as_view(success_url='.')),
    path('orders/', views.OrderView.as_view()),
    path('orders/<int:pk>/update', views.OrderUpdate.as_view(success_url='..')),
    path('orders/<int:id_order>/delete', views.delete_order),

    path('customers/create', views.CustomerCreate.as_view(success_url='.')),
    path('customers/', views.CustomerView.as_view()),
    path('customers/<int:pk>/update', views.CustomerUpdate.as_view(success_url='..')),
    path('customers/<int:id_customer>/delete', views.delete_customer),
    path('customers/<int:id_customer>/orders', views.customer_orders),

    path('models/create', views.ModelTechniqueCreate.as_view(success_url='.')),
    path('models/', views.ModelTechniqueView.as_view()),
    path('models/<int:pk>/update', views.ModelTechniqueUpdate.as_view(success_url='..')),
    path('models/<int:id_model>/delete', views.delete_model),

    path('technique/create', views.TechniqueCreate.as_view(success_url='.')),
    path('technique/', views.TechniqueView.as_view()),
    path('technique/<int:pk>/update', views.TechniqueUpdate.as_view(success_url='..')),
    path('technique/<int:id_technique>/delete', views.delete_technique),

    path('masters/create', views.MasterCreate.as_view(success_url='.')),
    path('masters/', views.MasterView.as_view()),
    path('masters/<int:pk>/update', views.MasterUpdate.as_view(success_url='..')),
    path('masters/<int:id_master>/delete', views.delete_master),

    path('price_list/create', views.PriceListCreate.as_view(success_url='.')),
    path('price_list/', views.PriceListView.as_view()),
    path('price_list/<int:pk>/update', views.PriceListUpdate.as_view(success_url='..')),
    path('price_list/<int:pk>/delete', views.delete_price),

]
