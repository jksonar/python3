# SSL Expiration Check Script

import ssl
import socket
from datetime import datetime, timezone

def get_ssl_expiry(domain):
    context = ssl.create_default_context()
    
    try:
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                expiry_date_str = cert['notAfter']
                expiry_date = datetime.strptime(expiry_date_str, '%b %d %H:%M:%S %Y %Z')
                
                # Make expiry_date timezone-aware (UTC)
                expiry_date = expiry_date.replace(tzinfo=timezone.utc)
                
                return expiry_date
    except Exception as e:
        return f"Error: {e}"

def check_ssl_expiry(domain):
    expiry_date = get_ssl_expiry(domain)
    
    if isinstance(expiry_date, datetime):
        now_utc = datetime.now(timezone.utc)
        remaining_days = (expiry_date - now_utc).days
        print(f"Domain: {domain}")
        print(f"SSL Expiration Date: {expiry_date}")
        print(f"Days Remaining: {remaining_days}")
        
        if remaining_days < 30:
            print("⚠️ Warning: SSL certificate expires soon!")
        else:
            print("✅ SSL certificate is valid.")
    else:
        print(expiry_date)

if __name__ == "__main__":
    domain_list = [
        "example.com",
        "google.com",
        "www.yahoo.in"
    ]
    
    for domain in domain_list:
        print("-" * 40)
        check_ssl_expiry(domain)
