from django.test import TestCase
from django.urls import reverse
from itertools import cycle

from . import baker_recipes as recipes
from .models import Warehouse, Product


class WarehouseManagementTestCase(TestCase):
    def setUp(self) -> None:
        (
            self.warehouses,
            self.products,
            self.inventories,
            self.inventory_movements,
        ) = recipes.seed(scale=10)
        self.warehouse_url = reverse("warehouse-list")
        self.product_url = reverse("product-list")

    ############################################################################
    #                       warehouse tests                                    #
    ############################################################################

    def test_get_warehouses(self):
        # with self.assertNumQueries(1):
        response = self.client.get(self.warehouse_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 10)

    def test_get_warehouse(self):
        warehouse = self.warehouses[0]
        url = reverse("warehouse-detail", kwargs={"pk": warehouse.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], warehouse.id)

    ############################################################################
    #                       product tests                                      #
    ############################################################################
    def test_get_products(self):
        response = self.client.get(self.product_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1000)

    def test_get_product(self):
        product = self.products[0]
        url = reverse("product-detail", kwargs={"pk": product.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], product.id)

    ############################################################################
    #                       product tests                                      #
    ############################################################################
    def test_get_inventories(self):
        response = self.client.get(self.inventory_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 100)

    def test_get_inventory(self):
        inventory = self.inventories[0]
        url = reverse("inventory-detail", kwargs={"pk": inventory.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], inventory.id)
