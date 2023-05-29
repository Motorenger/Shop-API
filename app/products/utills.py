from django.shortcuts import get_object_or_404

from carts.models import Cart
from products.models import Product


def get_cart(request):
    cart = get_object_or_404(Cart, id=request.session["cart_id"])
    return cart


def get_product(product_id: int):
    product = get_object_or_404(Product, id=product_id)
    return product
