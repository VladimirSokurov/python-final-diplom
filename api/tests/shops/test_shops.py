import pytest

from shops.models import ProductInfo


@pytest.mark.django_db
def test_view_products(client, product_create_factory):
    product_create_factory(_quantity=2)
    product_info = ProductInfo.objects.all()

    url = '/api/v1/products/'
    resp = client.get(url)

    assert len(resp.data) == 2
    assert len(resp.data) == len(product_info)
    assert resp.status_code == 200
