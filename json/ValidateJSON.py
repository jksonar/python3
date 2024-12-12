import json

# To check if a string is valid JSON

def is_valid_json(json_string):
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False

print(is_valid_json('{"name": "John"}'))  # Output: True
print(is_valid_json('{"name": "John"'))   # Output: False
