from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    # Auth
    path("auth/", include("users.urls")),

    path('admin/', admin.site.urls),
]
