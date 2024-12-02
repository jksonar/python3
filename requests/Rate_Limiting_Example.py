# Rate Limiting Example
import time
import requests

for i in range(10):
    response = requests.get('https://example.com/api')
    print(response.status_code)
    time.sleep(1)  # Wait 1 second between requests
