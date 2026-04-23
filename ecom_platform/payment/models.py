from django.db import models
from orders.models import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)

    INITIATED = "IN"
    SUCCESS = "SC"
    FAILED = "FL"

    STATUS_CHOICES = [
        (INITIATED, "Initiated"),
        (SUCCESS, "Success"),
        (FAILED, "Failed"),
    ]

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=INITIATED
    )

    method = models.CharField(max_length=20)  # WALLET later

    reference_id = models.CharField(max_length=100, unique=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)