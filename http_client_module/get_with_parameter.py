import http.client
from urllib.parse import urlencode

def fetch_with_params():
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

    params = urlencode({"userId": 1})
    conn.request("GET", f"/posts?{params}")

    response = conn.getresponse()
    print("Status:", response.status)
    print("Body:", response.read().decode())
    
    conn.close()

fetch_with_params()
