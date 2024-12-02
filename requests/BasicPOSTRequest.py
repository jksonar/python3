# Basic POST Request
import requests

data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.json())
