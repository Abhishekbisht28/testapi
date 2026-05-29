from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'products',   views.ProductViewSet,  basename='product')
router.register(r'orders',     views.OrderViewSet,    basename='order')

urlpatterns = [
    # ViewSet routes (auto-generated)
    path('', include(router.urls)),

    # ── Fast endpoints ────────────────────────────────────────────────────────
    path('health/',    views.health_check,    name='health-check'),
    path('overview/',  views.api_overview,    name='api-overview'),
    path('search/',    views.product_search,  name='product-search'),

    # ── Slow endpoints (all >800ms — will be caught by tester) ───────────────
    path('report/',       views.generate_report,     name='generate-report'),     # 1200ms
    path('sync/',         views.sync_inventory,       name='sync-inventory'),      # 1500ms
    path('analytics/',    views.analytics_dashboard,  name='analytics-dashboard'), # 950ms
    path('export/',       views.export_orders,        name='export-orders'),       # 1100ms
    path('recommendations/', views.recommendations,   name='recommendations'),     # 1300ms
    path('notifications/',views.notifications,        name='notifications'),       # 900ms
    path('audit-log/',    views.audit_log,            name='audit-log'),           # 1400ms
    path('dashboard/',    views.full_dashboard,       name='full-dashboard'),      # 1600ms
    path('price-update/', views.bulk_price_update,    name='price-update'),        # 1050ms
    path('warehouse/',    views.warehouse_status,     name='warehouse-status'),    # 1250ms
    path('forecast/',     views.demand_forecast,      name='demand-forecast'),     # 1800ms
    path('email-campaign/',views.send_email_campaign, name='email-campaign'),      # 2000ms
    path('invoices/',     views.invoice_generator,    name='invoice-generator'),   # 1350ms
]