# Sample Django REST Framework Project

A simple e-commerce API with Categories, Products, and Orders.
Used for testing with **api-response-time-tester**.

## Endpoints

| Method | URL                        | Description           |
|--------|----------------------------|-----------------------|
| GET    | /api/                      | List all routes       |
| GET    | /api/health/               | Health check          |
| GET    | /api/search/               | Search products       |
| POST   | /api/search/               | Search by name (body) |
| GET    | /api/categories/           | List categories       |
| POST   | /api/categories/           | Create category       |
| GET    | /api/categories/{pk}/      | Get category          |
| PUT    | /api/categories/{pk}/      | Update category       |
| PATCH  | /api/categories/{pk}/      | Partial update        |
| DELETE | /api/categories/{pk}/      | Delete category       |
| GET    | /api/products/             | List products         |
| POST   | /api/products/             | Create product        |
| GET    | /api/products/{pk}/        | Get product           |
| PUT    | /api/products/{pk}/        | Update product        |
| PATCH  | /api/products/{pk}/        | Partial update        |
| DELETE | /api/products/{pk}/        | Delete product        |
| GET    | /api/orders/               | List orders           |
| POST   | /api/orders/               | Create order          |
| GET    | /api/orders/{pk}/          | Get order             |
| PUT    | /api/orders/{pk}/          | Update order          |
| PATCH  | /api/orders/{pk}/          | Partial update        |
| DELETE | /api/orders/{pk}/          | Delete order          |

## Quick Start

```bash
pip install -r requirements.txt
python manage.py migrate
python seed.py        # loads sample data
python manage.py runserver
```

Server runs at http://localhost:8000
