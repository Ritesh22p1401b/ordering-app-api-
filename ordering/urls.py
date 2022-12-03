from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('User_Authenticatee.urls')),
    path('order/',include('order.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

