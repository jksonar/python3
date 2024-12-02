# DELETE Request
import requests

response = requests.delete('https://api.example.com/resource/1')
print(response.status_code)
