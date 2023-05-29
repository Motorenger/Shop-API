from rest_framework import generics, filters, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from products.models import Product
from products.serializers import ProductSerializer, AddToCartSerializer
from carts.models import CartProductM2M
from products.utills import get_cart, get_product


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["type", "in_stock"]
    search_fields = ["title"]


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AddToCartView(generics.CreateAPIView):
    serializer_class = AddToCartSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart = get_cart(request=request)
        size = request.data.get("size")
        try:
            product_in_cart = CartProductM2M.objects.get(cart=cart, size=size)
        except CartProductM2M.DoesNotExist:
            product_in_cart = None
        if product_in_cart:
            product_in_cart.quantity += 1
            product_in_cart.save()
        else:
            CartProductM2M.objects.create(product=get_product(product_id=kwargs.get("pk")), cart=cart, size=size)

        return Response(status=status.HTTP_201_CREATED)
