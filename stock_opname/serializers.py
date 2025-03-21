from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    barcode = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.DecimalField(max_digits=10, decimal_places=2)