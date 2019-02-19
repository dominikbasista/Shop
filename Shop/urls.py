from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('orders.urls', namespace='order')),
    path('', include('shop.urls', namespace='shop')),

]
