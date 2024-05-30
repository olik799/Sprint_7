import allure
import pytest
from data import order_body
from base_metod import create_order


class TestCreateOrder:

    @allure.title('Создаем заказ')
    def test_create_order(self):
        response = create_order(order_body)
        assert response.status_code == 201 and type((response.json())['track']) == int

    @allure.title('Проверяем возможность заказа с различными комбинациями color')
    @pytest.mark.parametrize('key, value', [
        ['color', ['BLACK']],
        ['color', ['GREY']],
        ['color', ['BLACK', 'GREY']],
        ['color', []]
    ]
                             )
    def test_create_order_different_color(self, key, value):
        order_body['key'] = 'value'
        response = create_order(order_body)
        assert response.status_code == 201 and type((response.json())['track']) == int
