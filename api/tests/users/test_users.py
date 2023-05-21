import pytest


@pytest.mark.django_db
def test_user_registration(client, user_info):
    url = '/api/v1/user/register/'
    resp = client.post(url, data=user_info)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_contact(client, user_token):
    url = '/api/v1/user/contact/'
    resp = client.get(url)
    assert resp.status_code == 200
