"""
Run once to populate the database with sample data:
  python seed.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testapi.settings')
django.setup()

from store.models import Category, Product, Order

# Categories
electronics = Category.objects.create(name='Electronics',  description='Gadgets and devices')
clothing    = Category.objects.create(name='Clothing',      description='Apparel and accessories')
books       = Category.objects.create(name='Books',         description='Physical and digital books')

# Products
p1 = Product.objects.create(name='Laptop Pro',     price=999.99,  stock=10, category=electronics, description='High-performance laptop')
p2 = Product.objects.create(name='Wireless Mouse', price=29.99,   stock=50, category=electronics, description='Ergonomic wireless mouse')
p3 = Product.objects.create(name='T-Shirt XL',     price=19.99,   stock=100,category=clothing,    description='Cotton t-shirt')
p4 = Product.objects.create(name='Django for APIs',price=49.99,   stock=30, category=books,       description='Learn Django REST Framework')

# Orders
Order.objects.create(product=p1, quantity=1, status='confirmed')
Order.objects.create(product=p2, quantity=2, status='pending')
Order.objects.create(product=p3, quantity=3, status='shipped')
Order.objects.create(product=p4, quantity=1, status='delivered')

print("✅ Sample data created:")
print(f"   {Category.objects.count()} categories")
print(f"   {Product.objects.count()} products")
print(f"   {Order.objects.count()} orders")
