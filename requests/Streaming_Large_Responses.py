# Streaming Large Responses
import requests

response = requests.get('https://example.com/largefile', stream=True)
for chunk in response.iter_content(chunk_size=1024):
    print(chunk)
