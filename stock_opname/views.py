from django.shortcuts import render
from rest_framework.views import APIView

from engine.permissions import public_access, user_or_manager_required, manager_required
from .serializers import ProductSerializer
from .services import create_product, get_all_products, get_product_by_id, update_product, \
    delete_product


class ProductView(APIView):
    @public_access
    def get(self, request, product_id=None):
        context = {
            'products': get_all_products()
        }

        if product_id:
            product = get_product_by_id(product_id)
            context['product'] = product

        return render(request, 'landing.html', context)

    @user_or_manager_required
    def post(self, request, product_id=None):
        method = request.POST.get('_method', 'POST').upper()

        if method == 'PUT':
            return self.put(request, product_id)
        elif method == 'DELETE':
            return self.delete(request, product_id)

        serializer = ProductSerializer(data=request.data)
        context = {
            'products': get_all_products()
        }

        if serializer.is_valid(raise_exception=True):
            status, response = create_product(serializer.validated_data)
            context['response'] = response

        return render(request, 'landing.html', context)

    @user_or_manager_required
    def put(self, request, product_id=None):
        serializer = ProductSerializer(data=request.data)
        context = {
            'products': get_all_products()
        }

        if serializer.is_valid(raise_exception=True):
            status, response = update_product(product_id, serializer.validated_data)
            context['response'] = response

        return render(request, 'landing.html', context)

    @manager_required
    def delete(self, request, product_id):
        context = {
            'products': get_all_products()
        }

        status, response = delete_product(product_id)
        context['response'] = response

        return render(request, 'landing.html', context)
