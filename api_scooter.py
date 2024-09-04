import allure
import requests
import urls


class ScooterApi:

    @staticmethod
    @allure.step('Отправить запрос на создание курьера POST /api/v1/courier')
    def registration_courier(body):
        return requests.post(urls.BASE_URL + urls.COURIER, json=body)

    @staticmethod
    @allure.step('Отправить запрос на вход курьера в систему POST /api/v1/courier/login')
    def login_courier(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER, json=body)

    @staticmethod
    @allure.step('Отправить запрос на удаление курьера DELETE /api/v1/courier/:id')
    def delete_courier(id_courier, body):
        return requests.delete(urls.BASE_URL + urls.COURIER + id_courier, json=body)

    @staticmethod
    @allure.step('Отправить запрос на создание заказа POST /api/v1/orders')
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.ORDER, json=body)

    @staticmethod
    @allure.step('Отправить запрос на получение списка заказов GET /api/v1/orders')
    def get_list_orders():
        return requests.get(urls.BASE_URL + urls.ORDER)

    @staticmethod
    @allure.step('Отправить запрос на принятия заказа PUT /api/v1/orders/accept/:id')
    def order_accept(query):
        return requests.put(urls.BASE_URL + urls.ORDER_ACCEPT + query)

    @staticmethod
    @allure.step('Отправить запрос на получение заказа по номеру GET /api/v1/orders/track')
    def order_track(query):
        return requests.get(urls.BASE_URL + urls.ORDER_TRACK + query)

    @staticmethod
    @allure.step('Отправить запрос на отмену заказа PUT /api/v1/orders/cancel')
    def order_cancel(body):
        return requests.put(urls.BASE_URL + urls.ORDER_TRACK, json=body)
