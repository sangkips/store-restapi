from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
        
    
class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

