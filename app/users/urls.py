from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import RegisterView


app_name = "auth"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    # Auth(Simple JWT)
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
