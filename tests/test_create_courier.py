import allure
from data import generate_data_for_new_courier
from base_metod import create_courier, delete_courier


@allure.title('Курьера можно создать')
def test_create_courier():
    payload = generate_data_for_new_courier()
    response = create_courier(payload)
    assert response.status_code == 201
    delete_courier(payload)


@allure.title('Нельзя создать двух одинаковых курьеров')
def test_create_same_courier():
    payload = generate_data_for_new_courier()
    create_courier(payload)
    response = create_courier(payload)
    assert response.status_code != 201


@allure.title('Нельзя создать курьера без параметра login')
def test_create_courier_without_params_login():
    payload = generate_data_for_new_courier()
    response = create_courier(payload={
        "login": '',
        "password": payload['password'],
        "firstName": payload['firstName']
    })
    assert response.status_code != 201


@allure.title('Нельзя создать курьера без параметра password')
def test_create_courier_without_params_password():
    payload = generate_data_for_new_courier()
    response = create_courier(payload={
        "login": payload['login'],
        "password": '',
        "firstName": payload['firstName']
    })
    assert response.status_code != 201


@allure.title('Правильный код ответа 201')
def test_create_courier_check_status_code():
    payload = generate_data_for_new_courier()
    response = create_courier(payload)
    assert response.status_code == 201
    delete_courier(payload)


@allure.title('Успешный запрос возвращает ""ok":true"')
def test_create_courier_check_text():
    payload = generate_data_for_new_courier()
    response = create_courier(payload)
    assert response.text == '{"ok":true}'
    delete_courier(payload)


@allure.title('Если создаем курьера без логина, возвращается ошибка')
def test_message_create_courier_without_login():
    payload = generate_data_for_new_courier()
    response = create_courier(payload={
        "login": '',
        "password": payload['password'],
        "firstName": payload['firstName']
    })
    assert (response.json())['message'] == "Недостаточно данных для создания учетной записи"


@allure.title('Если создаем курьера без пароля, возвращается ошибка')
def test_message_create_courier_without_password():
    payload = generate_data_for_new_courier()
    response = create_courier(payload={
        "login": payload['login'],
        "password": '',
        "firstName": payload['firstName']
    })
    assert (response.json())['message'] == "Недостаточно данных для создания учетной записи"


@allure.title('При создании пользователя с логином, который уже есть, возвращается ошибка')
def test_create_same_courier():
    payload = generate_data_for_new_courier()
    create_courier(payload)
    response = create_courier(payload={
        "login": payload['login'],
        "password": '12345678',
        "firstName": payload['firstName']
    })
    assert (response.json())['message'] == "Этот логин уже используется. Попробуйте другой."
    delete_courier(payload)
