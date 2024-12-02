# Handle Redirects
import requests

response = requests.get('https://api.example.com/redirect', allow_redirects=True)
print(response.url)
