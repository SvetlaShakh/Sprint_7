import allure
from api_scooter import ScooterApi
import helpers
import data_scooter


class TestAcceptOrder:

    @allure.title('Проверка успешного запрса принятия заказа - код ответа 201')
    @allure.description('При отправке запроса с существующим id курьера и track номером заказа на ручку PUT '
                        '/api/v1/orders/accept/:id возвращается код ответа 200 с текстом "ok": True')
    def test_successful_accept_order(self, create_courier):
        body = create_courier
        response_courier = ScooterApi.login_courier(body)
        courier_id = response_courier.json()['id']
        response_order = ScooterApi.create_order(data_scooter.order_dict)
        track_order = response_order.json()['track']
        query = f'{track_order}?courierId={courier_id}'
        response = ScooterApi.order_accept(query)
        helpers.del_login_courier(response_courier)
        helpers.cansel_order(response_order)
        assert response.status_code == 200
        assert response.json() == data_scooter.response_text_assept_order_200

    @allure.title('Проверка запроса принятия заказа без указания id курьера - код ответа 400')
    @allure.description('При отправке запроса без указания id курьера и с существующим track номером заказа на ручку '
                        'PUT /api/v1/orders/accept/:id возвращается код ответа 400 с текстом '
                        '"Недостаточно данных для поиска"')
    def test_accept_order_without_id_bad_request(self):
        response_order = ScooterApi.create_order(data_scooter.order_dict)
        track_order = response_order.json()['track']
        query = f'{track_order}'
        response = ScooterApi.order_accept(query)
        helpers.cansel_order(response_order)
        assert response.status_code == 400
        assert response.json()['message'] == data_scooter.response_text_assept_order_400

    @allure.title('Проверка запроса принятия заказа без указания track номера заказа - код ответа 400')
    @allure.description('При отправке запроса с существующим id курьера и без указания track номера заказа на ручку '
                        'PUT /api/v1/orders/accept/:id возвращается код ответа 400 с текстом '
                        '"Недостаточно данных для поиска"')
    def test_accept_order_without_track_bad_request(self, create_courier):
        body = create_courier
        response_courier = ScooterApi.login_courier(body)
        courier_id = response_courier.json()['id']
        query = f'courierId={courier_id}'
        response = ScooterApi.order_accept(query)
        helpers.del_login_courier(response_courier)
        assert response.status_code == 400
        assert response.json()['message'] == data_scooter.response_text_assept_order_400

    @allure.title('Проверка запроса принятия заказа с несуществующим track номером заказа - код ответа 404')
    @allure.description('При отправке запроса с существующим id курьера и несуществующим track номером заказа на ручку '
                        'PUT /api/v1/orders/accept/:id возвращается код ответа 404 с текстом '
                        '"Заказа с таким id не существует"')
    def test_accept_order_not_existing_track_not_found(self, create_courier):
        body = create_courier
        response_courier = ScooterApi.login_courier(body)
        courier_id = response_courier.json()['id']
        track_order = 0000
        query = f'{track_order}?courierId={courier_id}'
        response = ScooterApi.order_accept(query)
        helpers.del_login_courier(response_courier)
        assert response.status_code == 404
        assert response.json()['message'] == data_scooter.response_text_assept_order_404_track_order

    @allure.title('Проверка запроса принятия заказа с несуществующим id курьера - код ответа 404')
    @allure.description('При отправке запроса с несуществующим id курьера и существующим track номером заказа на ручку '
                        'PUT /api/v1/orders/accept/:id возвращается код ответа 404 с текстом '
                        '"Курьера с таким id не существует"')
    def test_accept_order_not_existing_id_not_found(self):
        courier_id = 0000
        response_order = ScooterApi.create_order(data_scooter.order_dict)
        track_order = response_order.json()['track']
        query = f'{track_order}?courierId={courier_id}'
        response = ScooterApi.order_accept(query)
        helpers.cansel_order(response_order)
        assert response.status_code == 404
        assert response.json()['message'] == data_scooter.response_text_assept_order_404_id_courier
