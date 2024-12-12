import json

json1 = {"name": "John", "age": 30}
json2 = {"city": "New York", "skills": ["Python"]}

merged = {**json1, **json2}
print(merged)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'skills': ['Python']}
