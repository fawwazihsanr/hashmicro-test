from django.test import TestCase
from django.urls import reverse

from engine.registry import registry
from engine.views import reload_urlconf
from .models import Product


class ProductViewTests(TestCase):
    def setUp(self):
        registry.register('stock_opname', '/stock_opname')
        reload_urlconf()
        self.product = Product.objects.create(
            name="Wafer",
            barcode="123456789",
            price=10000,
            stock=10
        )
        self.base_url = reverse('product')
        self.product_url = reverse('product-edit', args=[self.product.id])

    # --------------------------
    # GET Method Tests
    # --------------------------

    def test_get_product_list(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Wafer")
        self.assertTemplateUsed(response, 'landing.html')

    def test_get_single_product(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'], self.product)


    # --------------------------
    # POST Method Tests (Create)
    # --------------------------

    def test_create_product_success(self):
        data = {
            'name': 'Wortel',
            'barcode': '987654321',
            'price': 1000,
            'stock': 5
        }
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.count(), 2)

    def test_create_product_missing_required_field(self):
        data = {
            'name': 'Incomplete Product',
            # Missing barcode
            'price': 3000,
            'stock': 3
        }
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, 400)


    # --------------------------
    # PUT Method Tests (Update)
    # --------------------------

    def test_update_product_success(self):
        data = {
            '_method': 'PUT',
            'name': 'Updated Product',
            'barcode': '999888777',
            'price': 2000,
            'stock': 20
        }
        response = self.client.post(self.product_url, data)
        self.assertEqual(response.status_code, 200)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')

    def test_update_non_existent_product(self):
        url = reverse('product-edit', args=[999])
        data = {'_method': 'PUT', 'name': 'Ghost Product'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)

    def test_update_product_invalid_data(self):
        data = {
            '_method': 'PUT',
            'name': '',  # Invalid empty name
            'barcode': '123456789',
            'price': 3000,
            'stock': 10
        }
        response = self.client.post(self.product_url, data)
        self.assertEqual(response.status_code, 400)

    # --------------------------
    # DELETE Method Tests
    # --------------------------

    def test_delete_product_success(self):
        data = {'_method': 'DELETE'}
        response = self.client.post(self.product_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.count(), 0)
