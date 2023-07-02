from django.urls import path

from products.views import ProductListView, ProductRetrieveView, AddToCartView


app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("<int:pk>/", ProductRetrieveView.as_view(), name="retrieve"),
    path("<int:pk>/add-to-cart/", AddToCartView.as_view(), name="add_to_cart"),
]
