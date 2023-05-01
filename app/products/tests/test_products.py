import pytest

from django.urls import reverse

from products.models import Product


pytestmark = pytest.mark.django_db


class TestProductsListView:
    def test_get_no_products(self, api_client):
        response = api_client.get(reverse('products:list'))

        assert response.status_code == 200
        assert response.json().get('results') == []

    def test_get_one_products(self, api_client, baker):
        baker.make(Product)
        response = api_client.get(reverse('products:list'))

        assert response.status_code == 200
        assert len(response.json().get('results')) == 1
        assert float(response.json().get('results')[0].get('price')) == 645


class TestProductsRetrieveView:
    def test_get_not_found(self, api_client):
        response = api_client.get(reverse('products:retrieve', args=(32,)))

        assert response.status_code == 404
        assert response.json().get('detail') == "Not found."

    def test_get_success(self, api_client, baker):
        product = baker.make(Product)
        response = api_client.get(reverse('products:retrieve', args=(product.id,)))

        assert response.status_code == 200
        assert float(response.json().get('price')) == 645
