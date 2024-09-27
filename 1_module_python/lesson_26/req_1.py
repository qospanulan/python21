import requests
from requests.models import Response

response = requests.get('https://httpbin.org/image/jpeg')

print(response.status_code)

with open('img1.jpeg', 'wb') as file:
    file.write(response.content)

