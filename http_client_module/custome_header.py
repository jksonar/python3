import http.client

def custom_headers():
    conn = http.client.HTTPSConnection("www.example.com")

    headers = {
        'User-Agent': 'MyPythonApp/1.0',
        'Authorization': 'Bearer your_token_here'
    }

    conn.request("GET", "/", headers=headers)
    response = conn.getresponse()

    print("Status:", response.status)
    print("Body:", response.read().decode())
    
    conn.close()

custom_headers()
