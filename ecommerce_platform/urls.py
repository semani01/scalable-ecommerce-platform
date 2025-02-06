from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='index'),  # Root URL
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),  # Authentication endpoints
    path('api/products/', include('products.urls')),  # Product catalog endpoints
    path('api/cart/', include('cart.urls')),  # Cart management endpoints
    path('api/orders/', include('orders.urls')),  # Order management endpoints
]
