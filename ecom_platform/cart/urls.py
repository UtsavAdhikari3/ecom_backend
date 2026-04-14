from django.urls import path
from .views import AddToCartView,GetCartView

urlpatterns = [
    path('add/', AddToCartView.as_view()),
    path('items/', GetCartView.as_view()),
]