# Proxy Support
import requests

proxies = {'http': 'http://10.10.1.10:3128', 'https': 'http://10.10.1.10:1080'}
response = requests.get('https://api.example.com', proxies=proxies)
print(response.status_code)
