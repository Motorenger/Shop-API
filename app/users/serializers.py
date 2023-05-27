from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import CustomUser
from carts.models import Cart
from carts.serializers import CartSerializer


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ("email", "password", "password2", "cart")
        depth = 1

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": _("Password fields didn't match.")}
            )

        attrs["cart"] = self.context.get("request").data.get("cart")
        return attrs

    def create(self, validated_data):

        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            cart=validated_data["cart"],
        )

        return user
