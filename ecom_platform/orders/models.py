from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    PENDING = "PN"
    PAID = "PD"
    DELIVERED = "DL"
    CANCELLED = "CL"

    ORDER_STATUS = [
        (PENDING, "Pending"),
        (PAID, "Paid"),
        (DELIVERED, "Delivered"),
        (CANCELLED, "Cancelled"),
    ]

    status = models.CharField(
        max_length=2,
        choices=ORDER_STATUS,
        default=PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
