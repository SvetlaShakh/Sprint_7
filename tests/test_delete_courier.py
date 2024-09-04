import allure
from api_scooter import ScooterApi
import data_scooter


class TestDeleteCourier:

    @allure.title('Проверка успешного удаления курьера - код ответа 200')
    @allure.description('При отправке запроса с указанием id курьера в querty параметре и теле запроса на ручку '
                        'DELETE /api/v1/courier/:id возвращается код ответа 200 с текстом "ok": True')
    def test_successful_delete_courier(self, create_courier):
        body = create_courier
        response = ScooterApi.login_courier(body)
        courier_id = f'/{response.json()['id']}'
        body = {'id': response.json()['id']}
        response_del = ScooterApi.delete_courier(courier_id, body)
        assert response_del.status_code == 200
        assert response_del.json() == data_scooter.response_text_delete_courier_200

    @allure.title('Проверка удаления курьера без указания id курьера в querty параметре - код ответа 400')
    @allure.description('При отправке запроса без указания id курьера в querty параметре и '
                        'с указанием id в теле запроса на ручку DELETE /api/v1/courier/:id возвращается код ответа 400 '
                        'с текстом "Недостаточно данных для удаления курьера"')
    def test_delete_courier_without_id_request_bad_request(self, create_courier):
        body = create_courier
        response = ScooterApi.login_courier(body)
        courier_id = '/'
        body = {'id': response.json()['id']}
        response_del = ScooterApi.delete_courier(courier_id, body)
        assert response_del.status_code == 400
        assert response_del.json()['message'] == data_scooter.response_text_delete_courier_400

    @allure.title('Проверка удаления курьера без указания id курьера в теле запроса - код ответа 400')
    @allure.description('При отправке запроса с указанием id курьера в querty параметре и '
                        'без указания id в теле запроса на ручку DELETE /api/v1/courier/:id возвращается код ответа 400 '
                        'с текстом "Недостаточно данных для удаления курьера"')
    def test_delete_courier_without_id_body_bad_request(self, create_courier):
        body = create_courier
        response = ScooterApi.login_courier(body)
        courier_id = f'/{response.json()['id']}'
        body = {}
        response_del = ScooterApi.delete_courier(courier_id, body)
        assert response_del.status_code == 400
        assert response_del.json()['message'] == data_scooter.response_text_delete_courier_400

    @allure.title('Проверка удаления курьера с несуществующим id курьера - код ответа 404')
    @allure.description('При отправке запроса с указанием  несуществуещего id курьера в querty параметре и '
                        'в теле запроса на ручку DELETE /api/v1/courier/:id возвращается код ответа 404 '
                        'с текстом "Курьера с таким id нет"')
    def test_delete_courier_not_existing_id_not_found(self, create_courier):
        body = create_courier
        ScooterApi.login_courier(body)
        courier_id = f'/000'
        body = {'id': '000'}
        response_del = ScooterApi.delete_courier(courier_id, body)
        assert response_del.status_code == 404
        assert response_del.json()['message'] == data_scooter.response_text_delete_courier_404
