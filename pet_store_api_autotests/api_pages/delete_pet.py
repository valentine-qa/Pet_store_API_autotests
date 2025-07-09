import allure
from pet_store_api_autotests.api_pages.api_requests import delete_request

def delete_pet_by_id(url, pet):
    endpoint = f'/v2/pet/'
    pet_id = pet.json()['id']
    headers = {
        'Content-Type': 'application/json'
    }
    url = url + endpoint + f'{pet_id}'

    with allure.step("Get pet by ID"):
        response = delete_request(url, headers)

    return response