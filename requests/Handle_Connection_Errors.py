# Handle Connection Errors
import requests

try:
    response = requests.get('https://nonexistent.example.com')
    print(response.status_code)
except requests.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")
