parameters_list = [['login', 'password'], ['login', 'first_name'], ['password', 'first_name']]
order_dict = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}
response_text_assept_order_200 = {'ok': True}
response_text_assept_order_400 = 'Недостаточно данных для поиска'
response_text_assept_order_404_track_order = 'Заказа с таким id не существует'
response_text_assept_order_404_id_courier = 'Курьера с таким id не существует'
response_text_delete_courier_200 = {'ok': True}
response_text_delete_courier_400 = 'Недостаточно данных для удаления курьера'
response_text_delete_courier_404 = 'Недостаточно данных для удаления курьера'
response_text_get_order_by_track_400 = 'Недостаточно данных для поиска'
response_text_get_order_by_track_404 = 'Заказ не найден'
response_text_login_courier_400 = 'Недостаточно данных для входа'
response_text_login_courier_404 = 'Учетная запись не найдена'
response_text_registration_courier_201 = {'ok': True}
response_text_registration_courier_400 = 'Недостаточно данных для создания учетной записи'
response_text_registration_courier_409 = 'Этот логин уже используется'