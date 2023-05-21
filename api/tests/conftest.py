import pytest
from model_bakery import baker
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from orders.models import Order
from shops.models import Category, Product, ProductInfo, Shop
from users.models import Contact, User


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user_token(client):
    user = User.objects.create_user(email='1@yandex.ru', username='username1', password='PassW0rd1', is_active=True)
    token = Token.objects.create(user=user)
    return client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')


@pytest.fixture
def user_info():
    return {'first_name': 'firstname1',
            'last_name': 'lastname1',
            'email': '1@yandex.ru',
            'password': 'PassW0rd1',
            'password2': 'PassW0rd1',
            'username': 'username1',
            'company': 'company1',
            'position': 'position1',
            'type': 'buyer'}


@pytest.fixture
def product_create_factory():
    def factory(*args, **kwargs):
        shop = baker.make(Shop)
        category = baker.make(Category)
        product = baker.make(Product, category=category)
        return baker.make(ProductInfo, product=product, shop=shop, *args, **kwargs)

    return factory


@pytest.fixture
def contact_fixture():
    return {
        'user': User.objects.first(),
        'city': 'city1',
        'street': 'street1',
        'house': 'house1',
        'structure': 'structure1',
        'building': 'building1',
        'apartament': 'apartament1',
        'phone': 'phone1',
    }


@pytest.fixture
def order_factory(user_token):
    def factory(*args, **kwargs):
        contact = Contact.objects.create(
            user_id=1,
            city='city1',
            street='street1',
            house='house1',
            structure='structure1',
            building='building1',
            apartment='apartment1',
            phone='phone1')

        return baker.make(Order, user_id=1, contact=contact, *args, **kwargs)

    return factory
