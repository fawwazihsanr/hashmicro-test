# example_module/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='product'),
    path('/<int:product_id>', views.ProductView.as_view(), name='product-edit'),
]