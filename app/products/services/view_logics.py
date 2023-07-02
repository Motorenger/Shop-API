from rest_framework.exceptions import NotFound

from carts.models import Cart, CartProductM2M
from products.models import Product, ClothesSize


def add_to_cart_logic(product: Product, cart: Cart, size: CartProductM2M.Sizes):
        # checking if the product is available in this size
        try:
            if product.type == "clothes":
                size_avalability = product.clothes_sizes.get(size=size)
            elif product.type == "footwear":
                size_avalability = product.footwear_sizes.get(size=size)
        except ClothesSize.DoesNotExist:
            raise NotFound(detail="Size is not available")

        try:
            product_in_cart = CartProductM2M.objects.get(cart=cart, size=size)
        except CartProductM2M.DoesNotExist:
            product_in_cart = None
        # checking whether product with this size is already in the cart
        # if it is then quantity inreases otherwise we create new 
        if product_in_cart:
            product_in_cart.quantity += 1
            product_in_cart.save()
        else:
            CartProductM2M.objects.create(product=product, cart=cart, size=size)
