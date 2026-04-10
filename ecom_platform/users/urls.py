from django.urls import path
from .views import UserRegisterView, UserLoginView,MeView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('me/', MeView.as_view(), name='me'),
]