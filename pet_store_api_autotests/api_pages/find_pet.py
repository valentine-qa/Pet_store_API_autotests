import allure
import requests
from pet_store_api_autotests.api_pages.api_requests import get_request

def find_pet_by_id(url, pet):
    endpoint = f'/v2/pet/'
    pet_id = pet.json()['id']
    payload = {}
    headers = {
        'Content-Type': 'application/json'
    }
    url = url + endpoint + f'{pet_id}'

    with allure.step("Get pet by ID"):
        response = get_request(url, headers)

    return response
