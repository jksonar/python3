# Extract Response Headers
import requests

response = requests.get('https://example.com')
print(response.headers['Content-Type'])
