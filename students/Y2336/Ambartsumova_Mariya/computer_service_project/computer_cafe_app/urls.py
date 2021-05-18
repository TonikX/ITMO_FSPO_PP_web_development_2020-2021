from django.urls import path
from .views import *

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('makeOrder/', MakingOrderView.as_view(), name='new_order'),
    path('view_orders/', OrdersView.as_view(queryset=Order.objects.filter(user=2)), name='orders'),
    path('admin_view_orders/', OrdersView.as_view(), name='admins'),
    path('view_computers/', ComputersListView.as_view(), name='computers'),
    path('edit_order/<int:pk>/edit/', OrderUpdateView.as_view(), name='order_edit'),
    path('delete_order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
)
