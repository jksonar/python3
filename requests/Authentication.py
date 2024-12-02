# Authentication
import requests

response = requests.get('https://api.example.com/protected', auth=('username', 'password'))
print(response.status_code)
