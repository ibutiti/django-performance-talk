from django.contrib import admin

from .models import Warehouse, Product, Inventory, InventoryMovement


admin.site.register(Warehouse)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(InventoryMovement)
