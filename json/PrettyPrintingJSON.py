import json

# a. Format JSON String
data = {"name": "John", "age": 30, "skills": ["Python", "JavaScript"]}
json_string = json.dumps(data, indent=4, sort_keys=True)
print(json_string)

# b. Format JSON File
with open("data.json", "r") as file:
    data = json.load(file)

with open("formatted_data.json", "w") as file:
    json.dump(data, file, indent=4, sort_keys=True)
