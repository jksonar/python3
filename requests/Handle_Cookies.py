# Handle Cookies
import requests

cookies = {'session_id': '12345'}
response = requests.get('https://example.com', cookies=cookies)
print(response.cookies)
