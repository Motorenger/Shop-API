from carts.models import Cart


class CartMiddleware:
    'This middleware adds cart_id to session'
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.session.get('cart_id') is None:
            request.session['cart_id'] = Cart.objects.create().id
        response = self.get_response(request)

        return response
