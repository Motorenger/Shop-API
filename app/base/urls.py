from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Products
    path("products/", include("products.urls")),
    # Auth
    path("auth/", include("users.urls")),
    path("admin/", admin.site.urls),
]
