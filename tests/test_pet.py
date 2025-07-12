import json
from enum import unique

import allure
import pytest
import requests
from allure_commons.types import Severity

from pet_store_api_autotests.api_pages.add_new_pet import  add_a_new_pet
from pet_store_api_autotests.api_pages.find_pet import find_pet_by_id
from pet_store_api_autotests.api_pages.delete_pet import delete_pet_by_id
from pet_store_api_autotests.api_pages.find_pet import find_pet_by_status
from pet_store_api_autotests.utils.validate_schema import validate_response_to_json_schema


@allure.epic('Pet API')
@allure.feature('API Tests about pets')
@allure.link('https://petstore.swagger.io/', name='Swagger Petstore')
class TestPet:
    @allure.title('Add new pet to the store')
    @allure.story('Create pet')
    @allure.tag('API')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'https://github.com/valentine-qa')
    def test_add_a_new_pet(self, base_url):
        new_pet = add_a_new_pet(base_url, pet_name = 'Bobik')
        print(new_pet.json())

        with allure.step("Check status code 200"):
            assert new_pet.status_code == 200
        with allure.step(f"Check that pet name is Bobik"):
            assert new_pet.json()["name"] == 'Bobik'
        validate_response_to_json_schema(json_schema='post_pet.json', response=new_pet)

    @allure.title('Find pet by ID')
    @allure.story('Find pet')
    @allure.tag('API')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'https://github.com/valentine-qa')
    def test_find_pet_by_id(self, base_url):
        new_pet = add_a_new_pet(base_url, pet_name = 'Shusha')

        response = find_pet_by_id(base_url, new_pet)

        with allure.step("Check status code 200"):
            assert response.status_code == 200
        with allure.step("Check pet name by ID"):
            assert response.json()["name"] == 'Shusha'
        validate_response_to_json_schema(json_schema='get_pet.json', response=new_pet)

    @allure.title('Find all pets with status "sold"')
    @allure.story('Find pet')
    @allure.tag('API')
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'https://github.com/valentine-qa')
    def test_find_pet_by_status(self, base_url):
        response = find_pet_by_status(base_url, status='sold')

        with allure.step("Get status list"):
            status_list = [pet['status'] for pet in response.json()]
        with allure.step("Get unique status"):
            unique_statuses = set(status_list)
            overall_status = ', '.join(unique_statuses)

        with allure.step("Check status code 200"):
            assert response.status_code == 200
        with allure.step('Check that all pets have status "sold" '):
            assert overall_status == 'sold'

    @allure.title('Delete pet from the store')
    @allure.story('Delete pet')
    @allure.tag('API')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'https://github.com/valentine-qa')
    def test_delete_pet(self, base_url):
        new_pet = add_a_new_pet(base_url, pet_name='Shusha')
        response = find_pet_by_id(base_url, new_pet)

        with allure.step("Check pet name by ID"):
            assert response.json()["name"] == 'Shusha'
        response = delete_pet_by_id(base_url, new_pet)
        validate_response_to_json_schema(json_schema='delete_pet.json', response=response)

        with allure.step("Check status code 200"):
            assert response.status_code == 200
        with allure.step("Check that pet with ID was deleted"):
            assert response.json()["message"] == str(new_pet.json()["id"])

    def test_fail(self):
        return False

    @pytest.mark.skip()
    def test_skip(self):
        pass





