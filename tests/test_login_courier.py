import allure
from data import generate_data_for_new_courier
from base_metod import create_courier, signup_courier, delete_courier


@allure.title('Курьер может авторизоваться')
def test_courier_signup_correct_data():
    payload = generate_data_for_new_courier()
    create_courier(payload)
    response = signup_courier(payload)
    assert response.status_code == 200
    delete_courier(payload)


@allure.title('Курьер не может авторизоваться без логина')
def test_courier_not_signup_without_login():
    payload = generate_data_for_new_courier()
    create_courier(payload)
    response = signup_courier(payload={
        "login": '',
        "password": payload['password']
    })
    assert response.status_code == 400


@allure.title('Курьер не может авторизоваться без пароля')
def test_courier_not_signup_without_password():
    payload = generate_data_for_new_courier()
    create_courier(payload)
    response = signup_courier(payload={
        "login": payload['login'],
        "password": ''
    })
    assert response.status_code == 400


@allure.title('Система вернёт ошибку, если неправильно указать логин')
def test_error_with_invalid_login():
    payload = generate_data_for_new_courier()
    create_courier(payload)
    response = signup_courier(payload={
        "login": 12345,
        "password": payload['password']
    })
    assert (response.json())['message'] == 'Учетная запись не найдена'


@allure.title('Система вернёт ошибку, если неправильно указать пароль')
def test_error_with_invalid_password():
    payload = generate_data_for_new_courier()
    create_courier(payload)
    response = signup_courier(payload={
        "login": payload['login'],
        "password": 'abc'
    })
    assert (response.json())['message'] == 'Учетная запись не найдена'


@allure.title('Система вернёт ошибку, если не указать логин')
def test_error_without_login():
    payload = generate_data_for_new_courier()
    create_courier(payload)
    response = signup_courier(payload={
        "login": '',
        "password": payload['password']
    })
    assert (response.json())['message'] == 'Недостаточно данных для входа'


@allure.title('Система вернёт ошибку, если не указать пароль')
def test_error_without_password():
    payload = generate_data_for_new_courier()
    create_courier(payload)
    response = signup_courier(payload={
        "login": payload['login'],
        "password": ''
    })
    assert (response.json())['message'] == 'Недостаточно данных для входа'


@allure.title('Система вернёт ошибку, если указать несуществующий логин')
def test_error_with_invalid_login():
    payload = generate_data_for_new_courier()
    create_courier(payload)
    response = signup_courier(payload={
        "login": 'Abcdefgh',
        "password": payload['password']
    })
    assert (response.json())['message'] == 'Учетная запись не найдена'


@allure.title('Успешный запрос возвращает id')
def test_courier_signup_correct_data_return_id():
    payload = generate_data_for_new_courier()
    create_courier(payload)
    response = signup_courier(payload={
        "login": payload['login'],
        "password": payload['password']
    })
    assert 'id' in response.text
    delete_courier(payload)
