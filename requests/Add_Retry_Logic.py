import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

# Create a session
session = requests.Session()

# Configure retries
retry = Retry(
    total=3,                # Total number of retries
    backoff_factor=0.5,     # Wait time between retries: 0.5, 1.0, 2.0, etc.
    status_forcelist=[500, 502, 503, 504]  # Retry on these HTTP status codes
)

# Mount retries to HTTP/HTTPS
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Perform a request
response = session.get('https://example.com')
print(response.status_code)
