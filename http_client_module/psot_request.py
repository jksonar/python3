import http.client
import json

def send_post():
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

    # Data to send
    payload = json.dumps({"title": "foo", "body": "bar", "userId": 1})

    headers = {
        'Content-Type': 'application/json'
    }

    # Send POST request
    conn.request("POST", "/posts", body=payload, headers=headers)

    response = conn.getresponse()
    print("Status:", response.status)
    print("Response:", response.read().decode())
    
    conn.close()

send_post()
