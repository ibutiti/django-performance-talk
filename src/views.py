from rest_framework.viewsets import ModelViewSet

from .models import Inventory, InventoryMovement, Product, Warehouse
from . import serializers


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = serializers.InventorySerializer

    def get_queryset(self):
        return (
            Inventory.objects.all()
            .prefetch_related("movements")
            .select_related("warehouse", "product")
        )


class InventoryMovementViewSet(ModelViewSet):
    queryset = InventoryMovement.objects.all()
    serializer_class = serializers.InventoryMovementSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = super(ProductViewSet, self).get_queryset()
        return queryset.prefetch_related("inventories__movements")

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.SlimProductSerializer
        return serializers.ProductSerializer


class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = serializers.WarehouseSerializer

    def get_queryset(self):
        if self.action == "list":
            return Warehouse.objects.all().prefetch_related("inventories__movements")
        return Warehouse.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.SlimWarehouseSerializer
        return serializers.WarehouseSerializer
