from django.urls import path
from .views import InitiatePaymentView


urlpatterns = [
    path('initiate_payment/', InitiatePaymentView.as_view()),
]