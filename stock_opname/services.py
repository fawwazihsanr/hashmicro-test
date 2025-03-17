from django.db import transaction

from stock_opname.models import Product


def create_product(data):
    with transaction.atomic():
        try:
            Product.objects.create(**data)
            return True, 'Successfully created product'
        except Exception as e:
            return False, str(e)

def get_all_products():
    products = Product.objects.all()
    return products

def get_product_by_id(product_id):
    product = Product.objects.filter(id=product_id).last()
    if product:
        return product
    return None

def update_product(product_id, data):
    with transaction.atomic():
        try:
            product = Product.objects.filter(pk=product_id).last()
            if not product:
                return False, 'Product not found'

            for key, value in data.items():
                setattr(product, key, value)
            product.save()
            return True, 'Successfully updated product'
        except Exception as e:
            return False, str(e)

def delete_product(product_id):
    with transaction.atomic():
        try:
            product = Product.objects.filter(pk=product_id).last()
            if not product:
                return False, 'Product not found'
            product.delete()
            return True, 'Successfully deleted product'
        except Exception as e:
            return False, str(e)
