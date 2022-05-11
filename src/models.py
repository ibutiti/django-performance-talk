from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Warehouse(models.Model):
    """
    Describes a warehouse.

    A warehouse has a name, a location and a capacity.
    Capacity is the maximum volume of products that
    can be stored in the warehouse.
    """

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    capacity = models.IntegerField()

    @property
    def occupied_capacity(self):
        """
        Returns the occupied capacity of the warehouse.
        """
        inventories = self.inventories.all()
        return sum(
            [
                inventory.total_warehouse_inventory * inventory.product.volume
                for inventory in inventories
            ]
        )

    @property
    def available_capacity(self):
        """
        Returns the available capacity of the warehouse.
        """
        return self.capacity - self.occupied_capacity

    def __str__(self):
        return f"WH {self.name} - {self.city}"


class Product(models.Model):
    """
    Describes a product.

    A product has a name, a description and a volume.
    For simplicity, we assume that the volume is:
        - always in the same unit
        - is not changeable
        - shapes don't matter
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    volume = models.IntegerField()

    @property
    def total_inventory(self):
        """
        Returns the total inventory of the product across all warehouses
        """
        inventories = self.inventories.all()
        total = sum([inventory.total_warehouse_inventory for inventory in inventories])

        return total

    def __str__(self):
        return f"Product {self.name}"


class Inventory(models.Model):
    """
    Describes a product's inventory in a specific warehouse.

    Only one inventory row per product per warehouse.
    """

    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, related_name="inventories"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="inventories"
    )

    class Meta:
        unique_together = ("warehouse", "product")

    @property
    def total_warehouse_inventory(self):
        """
        Returns the total inventory of a product in a warehouse.
        """
        movements = self.movements.all()
        total = 0
        for movement in movements:
            total = (
                total + movement.quantity
                if movement.movement_type == InventoryMovementTypes.IN
                else total - movement.quantity
            )

        return total

    def __str__(self):
        return f"Inventory {self.product} in {self.warehouse}"


class InventoryMovementTypes(models.IntegerChoices):
    """
    Describes different warehouse operations that result in the change of inventory.
    """

    IN = 1
    OUT = 0


class InventoryMovement(models.Model):
    """
    Describes an inventory movement.

    Each movement has a type, a quantity and a timestamp.
    """

    inventory = models.ForeignKey(
        Inventory, on_delete=models.CASCADE, related_name="movements"
    )
    movement_type = models.IntegerField(choices=InventoryMovementTypes.choices)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{InventoryMovementTypes(self.movement_type).name} by {self.quantity} at {self.timestamp.strftime('%H:%M %d/%m/%Y')}"
