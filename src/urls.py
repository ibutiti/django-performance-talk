from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register(r"warehouses", views.WarehouseViewSet, basename="warehouse")
router.register(r"products", views.ProductViewSet, basename="product")
router.register(r"inventory", views.InventoryViewSet, basename="inventory")
router.register(
    r"inventory-movements",
    views.InventoryMovementViewSet,
    basename="inventory-movement",
)

urlpatterns = router.urls
