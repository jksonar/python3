import http.client

def fetch_page():
    conn = http.client.HTTPSConnection("www.example.com")
    
    # Send GET request
    conn.request("GET", "/")

    # Get response
    response = conn.getresponse()
    print("Status:", response.status)
    print("Headers:", response.getheaders())
    print("Body:", response.read().decode())
    
    conn.close()

fetch_page()
