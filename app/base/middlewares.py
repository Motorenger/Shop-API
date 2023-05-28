from carts.models import Cart


class CartMiddleware:
    "This middleware adds cart_id to session"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            request.session["cart_id"] = request.user.cart.id
        elif request.session.get("cart_id") is None:
            request.session["cart_id"] = Cart.objects.create().id
        response = self.get_response(request)

        return response
