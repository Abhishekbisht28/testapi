from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer


# ── ModelViewSet-based views (auto-provides list, create, retrieve, update, destroy) ──

class CategoryViewSet(viewsets.ModelViewSet):
    queryset         = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset         = Order.objects.all()
    serializer_class = OrderSerializer


# ── Function-based views with @api_view ───────────────────────────────────────

@api_view(['GET'])
def health_check(request):
    """Simple health check endpoint."""
    return Response({'status': 'ok', 'message': 'API is running'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_overview(request):
    """Lists all available API endpoints."""
    routes = {
        'health':     '/api/health/',
        'overview':   '/api/',
        'categories': '/api/categories/',
        'products':   '/api/products/',
        'orders':     '/api/orders/',
    }
    return Response(routes, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def product_search(request):
    """
    GET  → returns all products (optionally filtered by ?name=)
    POST → creates a quick product lookup by name in body
    """
    if request.method == 'GET':
        name     = request.query_params.get('name', '')
        products = Product.objects.filter(name__icontains=name) if name else Product.objects.all()
        return Response(ProductSerializer(products, many=True).data)

    # POST
    name = request.data.get('name', '')
    products = Product.objects.filter(name__icontains=name)
    return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)
