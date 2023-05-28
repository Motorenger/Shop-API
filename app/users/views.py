from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import CustomUser
from users.serializers import RegisterSerializer
from carts.models import Cart, CartProductM2M
from carts.serializers import CartSerializer


class RegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        products = CartProductM2M.objects.filter(cart=request.session.get("cart_id"))
        products = [
            {
                "product_id": product.product.id,
                "quantity": product.quantity,
                "size": product.size,
                "price": product.price,
            }
            for product in products
        ]

        cart = Cart.objects.create()
        [
            cart.products.add(
                product["product_id"],
                through_defaults={
                    f: v for f, v in product.items() if f != "product_id"
                },
            )
            for product in products
        ]
        cart.save()
        request.data._mutable = True
        request.data["cart"] = cart
        request.data._mutable = False
        return super().create(request, *args, **kwargs)
