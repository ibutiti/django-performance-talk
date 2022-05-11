from rest_framework.viewsets import ModelViewSet

from .models import Inventory, InventoryMovement, Product, Warehouse
from .serializers import (
    InventorySerializer,
    InventoryMovementSerializer,
    ProductSerializer,
    WarehouseSerializer,
)


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryMovementViewSet(ModelViewSet):
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
