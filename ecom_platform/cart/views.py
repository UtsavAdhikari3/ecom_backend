from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Cart, CartItem
from products.models import Product
from .serializers import AddToCartSerializer

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddToCartSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        user = request.user
        product_id = serializer.validated_data["product_id"]
        quantity = serializer.validated_data["quantity"]

        try:
            product = Product.objects.get(id=product_id, is_active=True)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        cart, created = Cart.objects.get_or_create(user=user)

        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        new_quantity = cart_item.quantity + quantity if not item_created else quantity

        if new_quantity > product.stock:
            return Response({"error": "Exceeds available stock"}, status=400)

        cart_item.quantity = new_quantity
        cart_item.save()

        return Response({
            "message": "Item added to cart",
            "product": product.name,
            "quantity": cart_item.quantity
        }, status=200)


class DeleteCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        item_id = request.data.get("id")

        if not item_id:
            return Response(
                {"error": "Item ID required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            item = CartItem.objects.get(id=item_id, cart__user = user)
            item.delete()

            return Response({
                "success": True,
                "message": "Item deleted"
            })

        except CartItem.DoesNotExist:
            return Response(
                {"error": "Item not found"},
                status=status.HTTP_404_NOT_FOUND
            )

class GetCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response({
                "CartItems": [],
                "total_amount": 0
            }, status=200)

        items = cart.items.all()

        data = []
        total_amount = 0

        for item in items:
            subtotal = item.product.price * item.quantity
            total_amount += subtotal

            data.append({
                "id":item.id,
                "product": item.product.name,
                "quantity": item.quantity,
                "price": item.product.price,
                "subtotal": subtotal
            })

        return Response({
            "CartItems": data,
            "total_amount": total_amount
        }, status=200)