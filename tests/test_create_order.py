import allure
import pytest
from data import order_body
from base_metod import create_order


@allure.title('Создаем заказ')
def test_create_order():
    response = create_order(order_body)
    assert 'track' in response.text


@allure.title('Проверяем возможность заказа с различными комбинациями color')
@pytest.mark.parametrize('key, value', [
    ['color', ['BLACK']],
    ['color', ['GREY']],
    ['color', ['BLACK', 'GREY']],
    ['color', []]
]
                         )
def test_create_order_different_color(key, value):
    order_body['key'] = 'value'
    response = create_order(order_body)
    assert response.status_code == 201
