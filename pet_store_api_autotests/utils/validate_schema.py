import json

import allure
from jsonschema import validate

from pet_store_api_autotests.utils.path import abs_path_from_project


def validate_response_to_json_schema(json_schema, response):
    json_file = abs_path_from_project(f'pet_store_api_autotests/json_schemas/{json_schema}')

    with open(json_file) as file:
        with allure.step('Response shema validation'):
            validate(response.json(), schema=json.loads(file.read()))
