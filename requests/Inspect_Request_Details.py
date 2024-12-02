# Inspect Request Details
import requests

response = requests.get('https://example.com')
print(f"URL: {response.request.url}")
print(f"Headers: {response.request.headers}")
