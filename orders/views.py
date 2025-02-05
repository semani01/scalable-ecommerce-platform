from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only the orders belonging to the authenticated user
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically link the order to the authenticated user
        serializer.save(user=self.request.user)

class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return order items linked to the authenticated user's orders
        return OrderItem.objects.filter(order__user=self.request.user)
