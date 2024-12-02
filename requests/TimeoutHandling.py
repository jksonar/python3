# Timeout Handling
import requests

try:
    response = requests.get('https://api.example.com/resource', timeout=5)
    print(response.json())
except requests.exceptions.Timeout:
    print("Request timed out.")
