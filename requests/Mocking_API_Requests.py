# Mocking API Requests
import requests
from unittest.mock import patch

with patch('requests.get') as mock_get:
    mock_get.return_value.status_code = 200
    response = requests.get('https://example.com')
    print(response.status_code)
