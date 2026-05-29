from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router auto-generates all CRUD URLs for ViewSets
router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'products',   views.ProductViewSet,  basename='product')
router.register(r'orders',     views.OrderViewSet,    basename='order')

urlpatterns = [
    # ViewSet routes (list + detail for each)
    path('', include(router.urls)),

    # Function-based view routes
    path('health/',  views.health_check,  name='health-check'),
    path('search/',  views.product_search, name='product-search'),
]
