# Download a File
import requests

url = 'https://example.com/file.zip'
response = requests.get(url, stream=True)
with open('file.zip', 'wb') as file:
    for chunk in response.iter_content(chunk_size=1024):
        file.write(chunk)
