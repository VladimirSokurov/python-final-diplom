import pytest

from orders.models import Order


@pytest.mark.django_db
def test_get_order(order_factory, client, user_token):
    order_factory(_quantity=2)
    orders = Order.objects.filter(user_id=1)
    url = '/api/v1/order/'
    resp = client.get(url)

    assert len(resp.data) == 2
    assert len(resp.data) == len(orders)
    assert resp.status_code == 200
