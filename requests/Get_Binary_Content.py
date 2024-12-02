# Get Binary Content
import requests

response = requests.get('https://example.com/image.png')
with open('image.png', 'wb') as file:
    file.write(response.content)
