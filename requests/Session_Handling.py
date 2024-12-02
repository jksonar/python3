# Session Handling
import requests

session = requests.Session()
session.get('https://api.example.com/login')
response = session.get('https://api.example.com/data')
print(response.status_code)
