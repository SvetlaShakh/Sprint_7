import pytest
import allure
from api_scooter import ScooterApi
import helpers
import data_scooter


class TestRegistrationCourier:

    @allure.title('Проверка успешного создания курьера - код ответа 201')
    @allure.description('При отправке запроса с указанием данных login, password, first_name в теле запроса на ручку '
                        'POST /api/v1/courier возвращается код ответа 201 с текстом "ok": True')
    def test_successful_registration_courier(self):
        registration_body = helpers.generate_registration_body(10)
        response = ScooterApi.registration_courier(registration_body)
        helpers.del_created_courier(registration_body)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Проверка создания курьера без передачи одного из параметров '
                  'login, password, first_name - код ответа 400')
    @allure.description('При отправке запроса без указанием данных одного из параметров login, password, first_name '
                        'в теле запроса на ручку POST /api/v1/courier возвращается код ответа 400 '
                        'с текстом "Недостаточно данных для создания учетной записи"')
    @pytest.mark.parametrize('parm_1, parm_2', data_scooter.parameters_list)
    def test_registration_courier_without_parameter_bad_request(self, parm_1, parm_2):
        registration_body = helpers.generate_registration_body_two_parameters(parm_1, parm_2, 10)
        response = ScooterApi.registration_courier(registration_body)
        if response.status_code == 201:
            helpers.del_created_courier(registration_body)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Проверка повторного создания курьера с теми же данными - код ответа 409')
    @allure.description('При отправке запроса с указанием данных ранее зарегестированного курьера '
                        'в теле запроса на ручку POST /api/v1/courier возвращается код ответа 409 '
                        'с текстом "Этот логин уже используется"')
    def test_registration_courier_existing_courier_parameters_conflict(self):
        registration_body = helpers.generate_registration_body(10)
        ScooterApi.registration_courier(registration_body)
        response = ScooterApi.registration_courier(registration_body)
        helpers.del_created_courier(registration_body)
        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется'
