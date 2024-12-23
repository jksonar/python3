import http.client

def handle_errors():
    conn = http.client.HTTPSConnection("www.example.com")

    try:
        conn.request("GET", "/nonexistent")
        response = conn.getresponse()

        if response.status == 404:
            print("Error 404: Not Found")
        else:
            print("Response:", response.read().decode())
    
    except http.client.HTTPException as e:
        print(f"HTTP Exception: {e}")
    
    conn.close()

handle_errors()
