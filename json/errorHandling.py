import json
import datetime

# a. Handle JSON Decode Error
try:
    data = json.loads('{"name": "John", "age": 30,')  # Invalid JSON
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

# b. Handle Non-Serializable Objects
try:
    data = {"name": "John", "age": 30, "time": datetime.datetime.now()}
    json_string = json.dumps(data)
except TypeError as e:
    print(f"Error serializing JSON: {e}")
