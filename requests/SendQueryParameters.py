#  Send Query Parameters
import requests

params = {'q': 'python', 'page': 2}
response = requests.get('https://api.example.com/search', params=params)
print(response.url)
