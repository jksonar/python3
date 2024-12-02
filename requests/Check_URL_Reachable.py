# Check if a URL is Reachable
import requests

response = requests.head('https://example.com')
print(response.status_code)
