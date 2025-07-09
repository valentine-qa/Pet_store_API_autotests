import allure
import requests
from pet_store_api_autotests.api_pages.api_requests import post_request
def add_a_new_pet(url, pet_name):
    import requests
    import json

    endpoint = '/v2/pet'

    payload = json.dumps({
        "name": pet_name,
    })
    headers = {
        'Content-Type': 'application/json'
    }

    url = url + endpoint

    with allure.step("Add a new pet to the store"):
        new_pet = post_request(url, headers=headers, data=payload)

    return new_pet