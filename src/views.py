from rest_framework.viewsets import ModelViewSet

from .models import Inventory, InventoryMovement, Product, Warehouse
from . import serializers


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = serializers.InventorySerializer

    # def get_queryset(self):
    #     return Inventory.objects.all().prefetch_related('movements')


class InventoryMovementViewSet(ModelViewSet):
    queryset = InventoryMovement.objects.all()
    serializer_class = serializers.InventoryMovementSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    # def get_queryset(self):
    #     if self.action == 'list':
    #         return Product.objects.all().prefetch_related('inventories__movements')
    #     return Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductSerializer
        return serializers.ProductSerializer


class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = serializers.WarehouseSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Warehouse.objects.all()
        return Warehouse.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.WarehouseSerializer
        return serializers.WarehouseSerializer
