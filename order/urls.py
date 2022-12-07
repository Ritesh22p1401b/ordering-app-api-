from django.urls import path
from .views import *

urlpatterns = [
    path('',OrderCreateListView.as_view(),name='orders'),
    path('<int:order_id>/',OrderDetailView.as_view(),name='orders-details'),
    path('order-status/<int:order_id>/',UpdateOrderStatus.as_view(),name='updata-orders-status'),
    path('user/<int:user_id>/order/',UserOrderView.as_view(),name='user-order'),
    path('user/<int:user_id>/order/<int:order_id>/',UserOrderDetailView.as_view(),name='user-orders-detail'),
]
