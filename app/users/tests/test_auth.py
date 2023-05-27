import pytest

from django.urls import reverse

from users.models import CustomUser


pytestmark = pytest.mark.django_db


class TestRegisterView:
    def test_post_with_correct_data(self, api_client, user_registration_data):
        response = api_client.post(reverse("auth:register"), user_registration_data)

        assert response.status_code == 201, "Status code of response must be 201"
        assert (
            response.json().get("email") == user_registration_data["email"]
        ), f'The response must contain {user_registration_data["email"]} for "email" field'

        assert CustomUser.objects.count() == 1, "The db must contain one user"
