import allure
from api_scooter import ScooterApi


class TestGetListOrders:

    @allure.title('Проверка успешного получения списка заказов - код ответа 200')
    @allure.description('При отправке запроса на ручку GET /api/v1/orders возвращается код ответа 200 '
                        'в ответе содердится список заказов "orders"')
    def test_successful_get_list_orders(self):
        response = ScooterApi.get_list_orders()
        list_orders = type(response.json()['orders'])
        assert response.status_code == 200
        assert list_orders == list
