# views.py
import uuid
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from orders.models import Order
from .models import Payment


@api_view(['POST'])
def initiate_payment(request):
    user = request.user
    order_id = request.data.get("order_id")

    try:
        order = Order.objects.get(id=order_id, user=user)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)

    if order.status != Order.PENDING:
        return Response({"error": "Order already processed"}, status=400)

    existing_payment = Payment.objects.filter(order=order).first()
    if existing_payment and existing_payment.status == Payment.SUCCESS:
        return Response({"message": "Already paid"}, status=200)

    if existing_payment and existing_payment.status == Payment.INITIATED:
        payment = existing_payment
    else:
        reference_id = str(uuid.uuid4())

        payment = Payment.objects.create(
            order=order,
            method="WALLET",
            reference_id=reference_id
        )

    return Response({
        "reference_id": payment.reference_id,
        "amount": order.total_amount,
        "method": payment.method
    })