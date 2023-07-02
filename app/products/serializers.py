from rest_framework import serializers

from products.models import Product
from carts.models import CartProductM2M


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "title", "type", "price", "price_currency", "retrieve_url")


class AddToCartSerializer(serializers.ModelSerializer):
    size = serializers.ChoiceField(choices=CartProductM2M.Sizes.choices)
    class Meta:
        model = CartProductM2M
        fields = ("size",)
