import allure
from helpers import generate_data_for_new_courier
from base_metod import create_courier, delete_courier
import response_texts


class TestCreateCourier:

    @allure.title('Курьера можно создать')
    def test_create_courier(self):
        payload = generate_data_for_new_courier()
        response = create_courier(payload)
        assert (response.status_code == 201 and response.text == response_texts.response_create_courier_success)
        delete_courier(payload)

    @allure.title('Нельзя создать курьера без параметра login')
    def test_create_courier_without_params_login(self):
        payload = generate_data_for_new_courier()
        response = create_courier(payload={
            "login": '',
            "password": payload['password'],
            "firstName": payload['firstName']
        })
        assert (response.status_code == 400 and (response.json())['message'] == response_texts.
                response_create_courier_without_login_or_password)

    @allure.title('Нельзя создать курьера без параметра password')
    def test_create_courier_without_params_password(self):
        payload = generate_data_for_new_courier()
        response = create_courier(payload={
            "login": payload['login'],
            "password": '',
            "firstName": payload['firstName']
        })
        assert (response.status_code == 400 and response.json()['message'] == response_texts.
                response_create_courier_without_login_or_password)

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_same_courier(self):
        payload = generate_data_for_new_courier()
        create_courier(payload)
        response = create_courier(payload)
        assert (response.status_code == 409 and response.json()['message'] == response_texts.
                response_create_courier_with_same_login)
