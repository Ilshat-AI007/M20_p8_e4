from django.urls import path
from .views import (
    CustomerListView, CustomerDetailView,
    SalesPersonListView, SalesPersonDetailView,
    ProductListView, ProductDetailView,
    SaleListView, SaleDetailView, IndexView
)

urlpatterns = [
    # Маршрут для корня сайта
    path('', IndexView.as_view(), name='index'),

    # Маршруты для покупателей
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    # Маршруты для продавцов
    path('salespersons/', SalesPersonListView.as_view(), name='salesperson-list'),
    path('salespersons/<int:pk>/', SalesPersonDetailView.as_view(), name='salesperson-detail'),

    # Маршруты для товаров
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Маршруты для продаж
    path('sales/', SaleListView.as_view(), name='sale-list'),
    path('sales/<int:pk>/', SaleDetailView.as_view(), name='sale-detail'),
]