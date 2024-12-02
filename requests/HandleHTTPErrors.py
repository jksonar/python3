# Handle HTTP Errors
import requests

response = requests.get('https://api.example.com/nonexistent')
if response.status_code == 404:
    print("Resource not found!")
