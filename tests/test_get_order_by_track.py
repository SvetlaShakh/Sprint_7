import allure
import helpers
from api_scooter import ScooterApi
import data_scooter


class TestGetOrderByTrack:

    @allure.title('Проверка успешного получения заказа по track номеру - код ответа 200')
    @allure.description('При отправке запроса c track номером в query параметре на ручку GET /api/v1/orders/track '
                        'возвращается код ответа 200 в ответе содердится объект с информацией о заказе "orders" '
                        'с track номером указанным при запросе')
    def test_successful_get_order_by_track(self):
        first_response = ScooterApi.create_order(data_scooter.order_dict)
        track = first_response.json()['track']
        query = f'?t={track}'
        response = ScooterApi.order_track(query)
        helpers.cansel_order(first_response)
        assert response.status_code == 200
        assert response.json()['order']['track'] == track

    @allure.title('Проверка получения заказа без указания track номера - код ответа 400')
    @allure.description('При отправке запроса без указания track номера на ручку GET /api/v1/orders/track '
                        'возвращается код ответа 400 с текстом "Недостаточно данных для поиска"')
    def test_get_order_without_track_bad_request(self):
        query = ''
        response = ScooterApi.order_track(query)
        assert response.status_code == 400
        assert response.json()['message'] == data_scooter.response_text_get_order_by_track_400

    @allure.title('Проверка получения заказа с указанием несуществующнго track номера - код ответа 404')
    @allure.description('При отправке запроса с указанием несуществующего track номера в query параметре на ручку '
                        'GET /api/v1/orders/track возвращается код ответа 404 с текстом "Заказ не найден"')
    def test_get_order_with_not_existing_track_not_found(self):
        query = f'?t=0000'
        response = ScooterApi.order_track(query)
        assert response.status_code == 404
        assert response.json()['message'] == data_scooter.response_text_get_order_by_track_404
