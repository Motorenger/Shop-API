from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "title", "type", "price", "price_currency", "retrieve_url")
