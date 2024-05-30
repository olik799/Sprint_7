import allure
from helpers import generate_data_for_new_courier
from base_metod import create_courier, signup_courier, delete_courier
import response_texts


class TestLoginCourier:

    @allure.title('Курьер может авторизоваться')
    def test_courier_signup_correct_data(self):
        payload = generate_data_for_new_courier()
        create_courier(payload)
        response = signup_courier(payload)
        assert response.status_code == 200 and type(response.json()['id']) == int
        delete_courier(payload)

    @allure.title('Курьер не может авторизоваться без логина')
    def test_courier_not_signup_without_login(self):
        payload = generate_data_for_new_courier()
        create_courier(payload)
        response = signup_courier(payload={
            "login": '',
            "password": payload['password']
        })
        assert (response.status_code == 400 and response.json()['message'] == response_texts.
                response_signup_without_login_or_password)

    @allure.title('Курьер не может авторизоваться без пароля')
    def test_courier_not_signup_without_password(self):
        payload = generate_data_for_new_courier()
        create_courier(payload)
        response = signup_courier(payload={
            "login": payload['login'],
            "password": ''
        })
        assert (response.status_code == 400 and response.json()['message'] == response_texts.
                response_signup_without_login_or_password)

    @allure.title('Система вернёт ошибку, если неправильно указать логин')
    def test_error_with_invalid_login(self):
        payload = generate_data_for_new_courier()
        create_courier(payload)
        response = signup_courier(payload={
            "login": 12345,
            "password": payload['password']
        })
        assert (response.status_code == 404 and response.json()['message'] == response_texts.
                response_signup_with_invalid_login_or_password)

    @allure.title('Система вернёт ошибку, если неправильно указать пароль')
    def test_error_with_invalid_password(self):
        payload = generate_data_for_new_courier()
        create_courier(payload)
        response = signup_courier(payload={
            "login": payload['login'],
            "password": 'abc'
        })
        assert (response.status_code == 404 and response.json()['message'] == response_texts.
                response_signup_with_invalid_login_or_password)
