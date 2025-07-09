import allure
import requests
import json
import jsonschema
from allure_commons._allure import step
from allure_commons.types import AttachmentType

url = "https://reqres.in/api/users"

payload = json.dumps({
  "name": "morpheus",
  "job": "leader"
})
headers = {
  'Content-Type': 'application/json',
  'x-api-key': 'reqres-free-v1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


def test():
  response = requests.request("POST", url, headers=headers, data=payload)
  body = response.json()
  assert response.status_code == 201
  with open("post_users.json") as file:
    jsonschema.validate(body, schema=json.loads(file.read()))


def reqres_api_get(url):
    requests.get()



def test_job_name_returns_in_response():
  job = "leader"
  name = "morpheus"
  with step("API Request"):
    response = requests.request("POST", url, headers=headers, data=payload)
    body = response.json()
    allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response", attachment_type=AttachmentType.JSON, extension="json")
    assert body["name"] == name
    assert body["job"] == job


def test_single_user():
  url = "https://reqres.in/api/users"
  response = requests.request("GET", url, params={"page": 2, "per_page": 4}, headers=headers)
  ids = [element["id"] for element in response.json()["data"]]
  set_ids = set(ids)
  set_ids = set_ids[1:]
  print()
