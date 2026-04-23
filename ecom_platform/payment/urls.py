from django.urls import path
from .views import InitiatePaymentView,ConfirmPaymentView


urlpatterns = [
    path('initiate_payment/', InitiatePaymentView.as_view()),
    path('confirm_payment/', ConfirmPaymentView.as_view()),
]