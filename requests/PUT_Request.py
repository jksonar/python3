# PUT Request
import requests

data = {"name": "updated_name"}
response = requests.put('https://api.example.com/resource/1', json=data)
print(response.json())
