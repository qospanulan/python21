import requests
import json

base_url = 'https://reqres.in'

get_users_url = f'{base_url}/api/users'

data = {
    "name": "Test User",
    "job": "Hunter"
}

response = requests.post(get_users_url, data=data)


json_data = response.json()
print(type(json_data))
print(json_data)
print("\n\n================================================\n")

beautiful_output = json.dumps(json_data, indent=4)
print(type(beautiful_output))
print(beautiful_output)

# for user in json_data['data']:
#     print(user['first_name'])

# print(response.text)




