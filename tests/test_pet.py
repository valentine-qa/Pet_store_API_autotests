import allure
import requests

from pet_store_api_autotests.api_pages.add_new_pet import  add_a_new_pet
from pet_store_api_autotests.api_pages.find_pet import find_pet_by_id
from pet_store_api_autotests.api_pages.delete_pet import delete_pet_by_id


def test_add_a_new_pet(base_url):
    new_pet = add_a_new_pet(base_url, pet_name = 'Bobik')
    print(new_pet.json())

    with allure.step("Check status code 200"):
        assert new_pet.status_code == 200
    with allure.step(f"Check that pet name is Bobik"):
        assert new_pet.json()["name"] == 'Bobik'


def test_find_pet_by_id(base_url):
    new_pet = add_a_new_pet(base_url, pet_name = 'Shusha')

    response = find_pet_by_id(base_url, new_pet)


    with allure.step('Проверка, что API возвращает код статуса 200.'):
        assert response.status_code == 200
    with allure.step("Check pet name by ID"):
        assert response.json()["name"] == 'Shusha'

def test_delete_pet(base_url):
    new_pet = add_a_new_pet(base_url, pet_name='Shusha')
    response = find_pet_by_id(base_url, new_pet)
    with allure.step("Check pet name by ID"):
        assert response.json()["name"] == 'Shusha'
    response = delete_pet_by_id(base_url, new_pet)

    with allure.step('Проверка, что API возвращает код статуса 200.'):
        assert response.status_code == 200
    with allure.step("Check that pet with ID was deleted"):
        assert response.json()["message"] == str(new_pet.json()["id"])