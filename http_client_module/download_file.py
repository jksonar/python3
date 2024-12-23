import http.client

def download_file():
    conn = http.client.HTTPSConnection("www.example.com")
    conn.request("GET", "/somefile.txt")

    response = conn.getresponse()
    
    with open("downloaded_file.txt", "wb") as f:
        f.write(response.read())
    
    print("File downloaded.")
    conn.close()

download_file()
