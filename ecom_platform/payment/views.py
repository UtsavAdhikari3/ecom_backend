import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from .models import Payment


class InitiatePaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        order_id = request.data.get("order_id")

        if not order_id:
            return Response({"error": "order_id required"}, status=400)

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
        }, status=200)
    
class ConfirmPaymentView(APIView):

    def post(self, request):
        reference_id = request.data.get("reference_id")
        success = request.data.get("success")
        transaction_id = request.data.get("transaction_id")

        if not reference_id:
            return Response({"error": "reference_id required"}, status=400)

        try:
            payment = Payment.objects.get(reference_id=reference_id)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=404)

        order = payment.order

        if payment.status == Payment.SUCCESS:
            return Response({"message": "Already processed"}, status=200)

        if success:
            payment.status = Payment.SUCCESS
            payment.transaction_id = transaction_id

            order.status = Order.PAID
        else:
            payment.status = Payment.FAILED
            order.status = Order.CANCELLED

        payment.save()
        order.save()

        return Response({"message": "Payment updated"})