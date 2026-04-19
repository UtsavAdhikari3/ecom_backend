from django.urls import path
from .views import AddToCartView,GetCartView,DeleteCartItemView

urlpatterns = [
    path('add/', AddToCartView.as_view()),
    path('delete/', DeleteCartItemView.as_view()),
    path('items/', GetCartView.as_view()),
]