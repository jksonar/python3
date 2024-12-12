
# a. Fetch Data from an API
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = response.json()  # Parse JSON response into a Python dictionary
print(data)

# b. Save Python Logs in JSON Format
import logging
import json

logging.basicConfig(filename="logs.json", level=logging.INFO, format="%(message)s")

data = {"event": "user_login", "user": "admin", "status": "success"}
logging.info(json.dumps(data))
