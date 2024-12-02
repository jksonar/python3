# Disable SSL Verification
import requests

response = requests.get('https://example.com', verify=False)
print(response.status_code)
