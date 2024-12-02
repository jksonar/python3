# Custom Headers
import requests

headers = {'User-Agent': 'my-app'}
response = requests.get('https://api.example.com/resource', headers=headers)
print(response.text)
