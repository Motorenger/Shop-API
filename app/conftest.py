import pytest

from model_bakery import baker as model_baker

from rest_framework.test import APIClient

from djmoney.models.fields import Money


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_registration_data():
    return {
        "email": "user_email@email.com",
        "password": "user_password",
        "password2": "user_password",
    }


def price():
    return Money(amount=645, currency="USD")


@pytest.fixture
def baker():
    model_baker.generators.add("djmoney.models.fields.MoneyField", price)
    return model_baker
