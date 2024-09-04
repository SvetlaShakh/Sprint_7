import random
import string
import allure
from api_scooter import ScooterApi
import data_scooter


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Создать словарь с данными для регистрации курьера')
def generate_registration_body(length):
    registration_body = {}
    registration_body['login'] = generate_random_string(length)
    registration_body['password'] = generate_random_string(length)
    registration_body['first_name'] = generate_random_string(length)
    return registration_body


@allure.step('Создать словарь с данными для регистрации курьера - 2 параметра')
def generate_registration_body_two_parameters(parm_1, parm_2, length):
    registration_body = {}
    registration_body[parm_1] = generate_random_string(length)
    registration_body[parm_2] = generate_random_string(length)
    return registration_body
@allure.step('Создать словарь с данными для логина курьера в системе')
def create_login_body(login_body, del_parameter):
    del login_body[del_parameter]
    return login_body

@allure.step('Удалить созданного курьера вошедшего в систему')
def del_login_courier(response):
    courier_id = f'/{response.json()['id']}'
    body = {'id': response.json()['id']}
    ScooterApi.delete_courier(courier_id, body)


@allure.step('Удалить созданного курьера')
def del_created_courier(registration_body):
    body = registration_body
    if 'first_name' in body:
        del body['first_name']
    response = ScooterApi.login_courier(body)
    del_login_courier(response)


@allure.step('Отменить созданный заказ')
def cansel_order(response):
    ScooterApi.order_cancel(response.json())


@allure.step('Cоздать словарь для заказа')
def create_order_dict(color):
    order_dict = data_scooter.order_dict
    order_dict['color'] = color
    return order_dict
