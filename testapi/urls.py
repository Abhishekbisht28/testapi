from django.urls import path, include

urlpatterns = [
    path('api/',          include('store.urls')),
    path('api/overview/', __import__('store.views', fromlist=['api_overview']).api_overview),
]
