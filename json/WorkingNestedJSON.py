import json


# a. Access Nested Data
json_string = '{"person": {"name": "John", "age": 30, "address": {"city": "New York"}}}'
data = json.loads(json_string)
print(data["person"]["address"]["city"])  # Output: New York


# b. Update Nested JSON
data = {"person": {"name": "John", "age": 30}}
data["person"]["age"] = 31
print(json.dumps(data, indent=4))
