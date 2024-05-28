import allure
from data import order_keys
from base_metod import get_order_list


@allure.title('Проверяем, что в тело ответа возвращается список заказов')
def test_get_order_list():
    response = get_order_list()
    response_list = response.json()['orders']

    # Выбираем первый элемент из полученного списка и собираем ключи
    response_element = response_list[0]
    response_key = response_element.keys()

    # Проверим что ключи из элемента ответа совпадают с ключами заказа
    assert set(order_keys).issubset(response_key) is True
