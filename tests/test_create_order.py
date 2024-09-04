import pytest
import allure
import helpers
from api_scooter import ScooterApi


class TestCreateOrder:

    @allure.title('Проверка успешного запрса создания заказа - код ответа 201')
    @allure.description('При отправке запроса с заполненными обязательными полями, в поле цвет указан один из цветов/ '
                        'указаны два цвета/ цвет не указан, на ручку POST /api/v1/orders возвращается код ответа 201, '
                        'в теле ответа указан track номер заказа')
    @pytest.mark.parametrize('color', [['BLACK'], ['GRAY'], ['BLACK', 'GRAY'], []])
    def test_successful_create_order(self, color):
        order_dict = helpers.create_order_dict(color)
        response = ScooterApi.create_order(order_dict)
        helpers.cansel_order(response)
        assert response.status_code == 201
        assert 'track' in response.json()
