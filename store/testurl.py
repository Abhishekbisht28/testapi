import time
import random
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer


# ── ModelViewSet-based views ──────────────────────────────────────────────────

class CategoryViewSet(viewsets.ModelViewSet):
    queryset         = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset         = Order.objects.all()
    serializer_class = OrderSerializer


# ── Fast APIs (pass) ──────────────────────────────────────────────────────────

@api_view(['GET'])
def health_check(request):
    """Health check — instant."""
    return Response({'status': 'ok', 'message': 'API is running'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_overview(request):
    """Lists all available endpoints."""
    return Response({
        'health':        '/api/health/',
        'categories':    '/api/categories/',
        'products':      '/api/products/',
        'orders':        '/api/orders/',
        'report':        '/api/report/',
        'sync':          '/api/sync/',
        'analytics':     '/api/analytics/',
        'export':        '/api/export/',
        'recommendations': '/api/recommendations/',
        'notifications': '/api/notifications/',
        'audit-log':     '/api/audit-log/',
        'dashboard':     '/api/dashboard/',
        'price-update':  '/api/price-update/',
        'warehouse':     '/api/warehouse/',
        'forecast':      '/api/forecast/',
    }, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def product_search(request):
    """Search products — fast."""
    if request.method == 'GET':
        name     = request.query_params.get('name', '')
        products = Product.objects.filter(name__icontains=name) if name else Product.objects.all()
        return Response(ProductSerializer(products, many=True).data)
    name     = request.data.get('name', '')
    products = Product.objects.filter(name__icontains=name)
    return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)


# ── SLOW APIs — all exceed 800ms, will be caught by tester ───────────────────

@api_view(['GET'])
def generate_report(request):
    """
    Monthly sales report.
    BUG: Unoptimized aggregation — takes ~1200ms.
    """
    time.sleep(1.2)
    return Response({
        'report':         'monthly_sales',
        'total_orders':   Order.objects.count(),
        'total_products': Product.objects.count(),
        'categories':     Category.objects.count(),
        'generated_at':   '2026-05-29',
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def sync_inventory(request):
    """
    Sync inventory with external warehouse.
    BUG: Blocking external HTTP call — takes ~1500ms.
    """
    time.sleep(1.5)
    return Response({
        'status':   'synced',
        'products': Product.objects.count(),
        'message':  'Inventory sync complete',
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def analytics_dashboard(request):
    """
    Analytics dashboard data.
    BUG: N+1 query problem, no DB index — takes ~950ms.
    """
    time.sleep(0.95)
    products = Product.objects.all()
    return Response({
        'total_revenue':  sum(float(p.price) * p.stock for p in products),
        'total_products': products.count(),
        'low_stock':      [p.name for p in products if p.stock < 5],
        'avg_price':      round(sum(float(p.price) for p in products) / max(products.count(), 1), 2),
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def export_orders(request):
    """
    Export all orders to CSV format.
    BUG: Loads entire orders table into memory — takes ~1100ms.
    """
    time.sleep(1.1)
    orders = Order.objects.select_related('product').all()
    rows   = [{'id': o.id, 'product': o.product.name, 'quantity': o.quantity, 'status': o.status}
              for o in orders]
    return Response({'format': 'csv', 'total': len(rows), 'rows': rows}, status=status.HTTP_200_OK)


@api_view(['GET'])
def recommendations(request):
    """
    Product recommendations engine.
    BUG: ML model loaded on every request instead of cached — takes ~1300ms.
    """
    time.sleep(1.3)
    products = list(Product.objects.values('id', 'name', 'price'))
    return Response({
        'recommended': random.sample(products, min(3, len(products))),
        'reason':      'based on purchase history',
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def notifications(request):
    """
    Fetch user notifications.
    BUG: Polling external notification service with no timeout — takes ~900ms.
    """
    time.sleep(0.9)
    return Response({
        'unread': 3,
        'notifications': [
            {'id': 1, 'message': 'Your order has been shipped',  'read': False},
            {'id': 2, 'message': 'Flash sale starts tomorrow',   'read': False},
            {'id': 3, 'message': 'New product in Electronics',   'read': False},
        ]
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def audit_log(request):
    """
    Fetch full audit log.
    BUG: No pagination, fetches all records — takes ~1400ms.
    """
    time.sleep(1.4)
    return Response({
        'total':   1500,
        'logs': [
            {'event': 'product_created', 'user': 'admin', 'timestamp': '2026-05-29T10:00:00Z'},
            {'event': 'order_updated',   'user': 'admin', 'timestamp': '2026-05-29T10:05:00Z'},
            {'event': 'category_deleted','user': 'admin', 'timestamp': '2026-05-29T10:10:00Z'},
        ]
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def full_dashboard(request):
    """
    Admin dashboard — aggregates everything.
    BUG: Makes 5 separate DB calls sequentially — takes ~1600ms.
    """
    time.sleep(1.6)
    return Response({
        'orders':     Order.objects.count(),
        'products':   Product.objects.count(),
        'categories': Category.objects.count(),
        'revenue':    sum(float(p.price) * p.stock for p in Product.objects.all()),
        'pending':    Order.objects.filter(status='pending').count(),
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def bulk_price_update(request):
    """
    Bulk update product prices.
    BUG: Updates one by one in a loop instead of bulk_update — takes ~1050ms.
    """
    time.sleep(1.05)
    updated = Product.objects.count()
    return Response({
        'status':  'updated',
        'count':   updated,
        'message': f'{updated} products price-updated successfully',
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def warehouse_status(request):
    """
    Check warehouse stock levels.
    BUG: Calls warehouse microservice with no connection pool — takes ~1250ms.
    """
    time.sleep(1.25)
    return Response({
        'warehouse': 'Mumbai-WH1',
        'status':    'operational',
        'capacity':  '78%',
        'products':  Product.objects.count(),
        'last_sync': '2026-05-29T14:00:00Z',
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def demand_forecast(request):
    """
    Predict next month demand using historical data.
    BUG: Runs forecast model synchronously on web thread — takes ~1800ms.
    """
    time.sleep(1.8)
    products = Product.objects.all()
    return Response({
        'forecast_period': 'June 2026',
        'predictions': [
            {'product': p.name, 'predicted_demand': random.randint(10, 200)}
            for p in products
        ],
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def send_email_campaign(request):
    """
    Trigger a marketing email campaign.
    BUG: Sends emails synchronously instead of queuing — takes ~2000ms.
    """
    time.sleep(2.0)
    return Response({
        'status':     'sent',
        'recipients': 1200,
        'campaign':   request.data.get('campaign', 'weekly_newsletter'),
        'message':    'Campaign dispatched to all subscribers',
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def invoice_generator(request):
    """
    Generate PDF invoices for all pending orders.
    BUG: Generates PDFs in memory synchronously — takes ~1350ms.
    """
    time.sleep(1.35)
    orders = Order.objects.filter(status='pending')
    return Response({
        'generated': orders.count(),
        'format':    'PDF',
        'message':   f'{orders.count()} invoices generated',
    }, status=status.HTTP_200_OK)