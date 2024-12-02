# Parse Query Parameters
import requests

url = 'https://example.com?name=John&age=30'
response = requests.get(url)
print(response.url)
