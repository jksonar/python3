# Upload Files
import requests

files = {'file': open('example.txt', 'rb')}
response = requests.post('https://api.example.com/upload', files=files)
print(response.status_code)
