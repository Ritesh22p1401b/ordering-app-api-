from django.urls import path
from .views import *

urlpatterns = [
    path('',OrderCreateListView.as_view(),name='orders'),
    path('<int:order_id>/',OrderDetailView.as_view(),name='orders-details'),
]
