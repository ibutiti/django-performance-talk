from rest_framework import serializers

from .models import Warehouse, Product, Inventory, InventoryMovement, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )


class InventoryMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryMovement
        fields = ("id", "inventory", "quantity", "movement_type", "timestamp")


class InventorySerializer(serializers.ModelSerializer):
    movements = InventoryMovementSerializer(many=True, read_only=True)
    total_warehouse_inventory = serializers.IntegerField(read_only=True)

    class Meta:
        model = Inventory
        fields = (
            "id",
            "warehouse",
            "product",
            "total_warehouse_inventory",
            "movements",
        )


class WarehouseSerializer(serializers.ModelSerializer):
    inventories = InventorySerializer(many=True, read_only=True)
    occupied_capacity = serializers.IntegerField(read_only=True)
    available_capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = Warehouse
        fields = (
            "id",
            "name",
            "city",
            "capacity",
            "occupied_capacity",
            "available_capacity",
            "inventories",
        )


class ProductSerializer(serializers.ModelSerializer):
    inventories = InventorySerializer(many=True, read_only=True)
    total_inventory = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "volume",
            "total_inventory",
            "inventories",
        )
