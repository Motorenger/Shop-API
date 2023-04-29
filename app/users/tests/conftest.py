import pytest

from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_registration_data():
    return {
            'email': 'user_email@email.com',
            'password': 'user_password',
            'password2': 'user_password'
        }
