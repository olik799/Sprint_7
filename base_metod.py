import json
import allure
import requests
from confyg import URL_MAIN, API_METHOD_CREATE_COURIER, API_METHOD_LOGIN_COURIER, API_METHOD_CREATE_ORDER


@allure.title('Создаем курьера')
def create_courier(payload):
    return requests.post(URL_MAIN + API_METHOD_CREATE_COURIER, data=payload)


@allure.title('Авторизация курьера')
def signup_courier(payload):
    return requests.post(URL_MAIN + API_METHOD_LOGIN_COURIER, data=payload)


@allure.title('Удаляем созданного курьера')
def delete_courier(payload):
    response = requests.post(URL_MAIN + API_METHOD_LOGIN_COURIER, data=payload)
    id_courier = response.json()["id"]
    requests.delete(f'{URL_MAIN}{API_METHOD_CREATE_COURIER}/{id_courier}')


@allure.title('Создаем заказ')
def create_order(order_body):
    return requests.post(URL_MAIN + API_METHOD_CREATE_ORDER, data=json.dumps(order_body))


@allure.title('Получить список заказов')
def get_order_list():
    return requests.get(URL_MAIN + API_METHOD_CREATE_ORDER)