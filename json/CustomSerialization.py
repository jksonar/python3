import json

import datetime
# If your Python object is not directly serializable, you can define a custom function:
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()  # Serialize datetime as ISO 8601 string
        return super().default(obj)

data = {"event": "meeting", "time": datetime.datetime.now()}
json_string = json.dumps(data, cls=CustomEncoder)
print(json_string)
