import pytest
from api_scooter import ScooterApi
import helpers


@pytest.fixture()
def create_courier():
    registration_body = helpers.generate_registration_body(10)
    ScooterApi.registration_courier(registration_body)
    del registration_body['first_name']
    return registration_body
