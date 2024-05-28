import allure
import random
import string

order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

order_keys = ['id', 'courierId', 'firstName', 'lastName', 'address', 'metroStation', 'phone', 'rentTime', 'deliveryDate',
              'track', 'color', 'comment']


response_success = {
             "id": 2,
             "firstName": "Naruto",
             "lastName": "Uzumaki",
             "address": "Kanoha, 142 apt.",
             "metroStation": "1",
             "phone": "+7 800 355 35 35",
             "rentTime": 5,
             "deliveryDate": "2020-06-06T00:00:00.000Z",
             "track": 521394,
             "status": 1,
             "color": [
                 "BLACK"
             ],
             "comment": "Saske, come back to Kanoha",
             "cancelled": False,
             "finished": False,
             "inDelivery": False,
             "courierFirstName": "Kaneki",
             "createdAt": "2020-06-08T14:40:28.219Z",
             "updatedAt": "2020-06-08T14:40:28.219Z"
}


@allure.title('Генерируем данные для курьера: логин, пароль, имя')
def generate_data_for_new_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


