import json

# a. Convert Python to JSON (json.dumps)
data = {"name": "John", "age": 30, "is_employee": True}
json_string = json.dumps(data)
print(json_string)  # Output: '{"name": "John", "age": 30, "is_employee": true}'

# b. Convert JSON to Python (json.loads)
json_string = '{"name": "John", "age": 30, "is_employee": true}'
data = json.loads(json_string)
print(data)  # Output: {'name': 'John', 'age': 30, 'is_employee': True}
