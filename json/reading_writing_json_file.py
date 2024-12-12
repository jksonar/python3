import json

# a. Write JSON to a File
data = {"name": "Alice", "age": 25, "skills": ["Python", "Django"]}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # Pretty print with 4 spaces

# b. Read JSON from a File
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)  # Output: {'name': 'Alice', 'age': 25, 'skills': ['Python', 'Django']}
