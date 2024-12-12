import json
import datetime

def custom_decoder(obj):
    if "time" in obj:
        obj["time"] = datetime.datetime.fromisoformat(obj["time"])
    return obj

json_string = '{"event": "meeting", "time": "2024-12-11T10:00:00"}'
data = json.loads(json_string, object_hook=custom_decoder)
print(data)
