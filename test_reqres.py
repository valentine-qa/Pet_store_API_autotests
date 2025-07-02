import requests
import json
import jsonschema
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
