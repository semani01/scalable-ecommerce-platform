from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get_queryset(self):
        # Return only the cart belonging to the authenticated user
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Ensure the cart is linked to the authenticated user when created
        serializer.save(user=self.request.user)

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return cart items belonging to the authenticated user's cart
        return CartItem.objects.filter(cart__user=self.request.user)
