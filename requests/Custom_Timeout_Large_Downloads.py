# Custom Timeout for Large Downloads
import requests

response = requests.get('https://example.com/largefile', timeout=10)
print(response.status_code)
