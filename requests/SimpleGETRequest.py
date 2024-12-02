# Simple GET Request
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.json())
