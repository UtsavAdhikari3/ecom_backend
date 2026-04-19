from django.shortcuts import render
from cart.models import Cart, CartItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from orders.models import Order, OrderItem

from django.db import transaction
from django.db.models import F

class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response({"error": "Cart is empty"}, status=400)

        items = cart.items.select_related('product').all()

        if not items.exists():
            return Response({"error": "Cart is empty"}, status=400)

        with transaction.atomic():
            for item in items:
                product = item.product

                if product.stock < item.quantity:
                    return Response({
                        "error": f"{product.name} is out of stock"
                    }, status=400)

            total_amount = 0
            for item in items:
                total_amount += item.product.price * item.quantity

            order = Order.objects.create(
                user=user,
                total_amount=total_amount,
                status=Order.PENDING
            )

            order_items = []
            for item in items:
                product = item.product

                product.stock = F('stock') - item.quantity
                product.save()

                order_items.append(
                    OrderItem(
                        order=order,
                        product=product,
                        quantity=item.quantity,
                        price_at_purchase=product.price
                    )
                )

            OrderItem.objects.bulk_create(order_items)

            items.delete()

        return Response({
            "message": "Order placed successfully",
            "order_id": order.id
        }, status=201)
class GetOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        orders = Order.objects.filter(user=user)

        if not orders.exists():
            return Response({"error": "There are no orders"}, status=400)

        data = []

        for order in orders:
            items_data = []

            for item in order.items.all():
                items_data.append({
                    "product": item.product.name,
                    "quantity": item.quantity,
                    "price": item.price_at_purchase
                })

            data.append({
                "order_id": order.id,
                "total_amount": order.total_amount,
                "status": order.status,
                "items": items_data
            })

        return Response({
            "message": "Success",
            "orders": data
        }, status=200)

