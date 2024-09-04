import allure
import pytest
from api_scooter import ScooterApi
import helpers


class TestLoginCourier:

    @allure.title('Проверка успешного входа курьера в систему - код ответа 200')
    @allure.description('При отправке запроса с указанием данных login, password в теле запроса на ручку '
                        'POST /api/v1/courier/login возвращается код ответа 200 в ответе содержится id курьера')
    def test_successful_login_courier(self, create_courier):
        body = create_courier
        response = ScooterApi.login_courier(body)
        helpers.del_login_courier(response)
        assert response.status_code == 200
        assert 'id' in response.text

    @allure.title('Проверка входа курьера в систему без указания login или password - код ответа 400')
    @allure.description('При отправке запроса с указанием данных только login или password в теле запроса на ручку POST'
                        '/api/v1/courier/login возвращается код ответа 400 с текстом "Недостаточно данных для входа"')
    @pytest.mark.parametrize('del_parameter', ['login', 'password'])
    def test_login_courier_without_parameter_bad_request(self, create_courier, del_parameter):
        body = create_courier.copy()
        login_body = helpers.create_login_body(body, del_parameter)
        response = ScooterApi.login_courier(login_body)
        helpers.del_created_courier(create_courier)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Проверка входа курьера в систему с указанием несуществующего login - код ответа 404')
    @allure.description('При отправке запроса с указанием несуществующего login в теле запроса на ручку POST'
                        '/api/v1/courier/login возвращается код ответа 404 с текстом "Учетная запись не найдена"')
    def test_login_courier_not_existing_courier_not_found(self):
        body = helpers.generate_registration_body_two_parameters('login', 'password', 7)
        response = ScooterApi.login_courier(body)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'
