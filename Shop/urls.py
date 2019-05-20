from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='order')),
    path('account/', include('accounts.urls', namespace='account')),
    path('', include('shop.urls', namespace='shop')),

]
