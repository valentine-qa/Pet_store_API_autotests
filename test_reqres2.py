import requests
import json



def test_get_user():

    base_url = 'https://reqres.in'
    end_point = '/api/users/'
    user_id = 2

    url = f"{base_url}{end_point}{user_id}"

    payload = json.dumps({
      "name": "morpheus",
      "job": "leader"
    })
    headers = {
      'Content-Type': 'application/json',
      'x-api-key': 'reqres-free-v1'
    }

    response = requests.request("GET", url, headers=headers)
    body = response.json()

    print(body["data"]["id"])
    print(response.headers)

