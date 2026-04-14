from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    path('products/', include('products.urls'))
    # path('wallet/', include('wallet.urls')),
    # path('orders/', include('orders.urls')),
    # path('payment/', include('payment.urls')),
]