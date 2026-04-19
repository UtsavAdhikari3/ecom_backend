from django.urls import path
from .views import CheckoutView,GetOrderView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('', GetOrderView.as_view(), name='orders')
]