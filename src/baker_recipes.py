import random
from itertools import cycle
from typing import List

from model_bakery import baker
from model_bakery.recipe import Recipe, foreign_key
from faker import Faker
from .models import Warehouse, Product, Inventory, InventoryMovement

fake = Faker()


warehouse_factory = Recipe(
    Warehouse,
    city=fake.city,
    name=fake.company,
    capacity=lambda: random.randint(1000, 10000),
)

product_factory = Recipe(
    Product,
    name=fake.word,
    description=fake.text,
    volume=lambda: random.randint(10, 100),
)

inventory_factory = Recipe(
    Inventory,
    warehouse=foreign_key(warehouse_factory),
    product=foreign_key(product_factory),
)

inventory_movement_factory = Recipe(
    InventoryMovement, quantity=lambda: random.randint(1, 100)
)


def seed(scale=10):
    warehouses: List[Warehouse] = warehouse_factory.make(
        _quantity=scale, _bulk_create=True
    )
    products: List[Product] = product_factory.make(
        _quantity=100 * scale, _bulk_create=True
    )

    inventories = []
    product_buffer = cycle(products)
    for warehouse in warehouses:
        inventories.extend(
            inventory_factory.make(
                _quantity=scale, product=product_buffer, warehouse=warehouse
            )
        )

    inventories: List[Inventory] = Inventory.objects.bulk_create(
        inventories, batch_size=300, ignore_conflicts=True
    )
    movements = inventory_movement_factory.make(
        inventory=cycle(inventories), _quantity=1000 * scale
    )

    return warehouses, products, inventories, movements
