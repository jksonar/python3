# SSL Expiration Check with Email Alerts and Logging
import ssl
import socket
import logging
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timezone

# Configure Logging
logging.basicConfig(filename="ssl_check.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"
EMAIL_RECEIVER = "receiver_email@gmail.com"

def send_email_alert(domain, expiry_date, days_remaining):
    subject = f"⚠️ SSL Expiry Alert for {domain}"
    body = (f"The SSL certificate for {domain} will expire on {expiry_date}.\n"
            f"Only {days_remaining} days remaining.\n\n"
            "Please renew it to avoid any disruptions.")
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
            logging.info(f"Email alert sent for {domain}.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

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
        logging.error(f"Error retrieving SSL for {domain}: {e}")
        return f"Error: {e}"

def check_ssl_expiry(domain):
    expiry_date = get_ssl_expiry(domain)
    
    if isinstance(expiry_date, datetime):
        # Use timezone-aware UTC datetime
        now_utc = datetime.now(timezone.utc)
        remaining_days = (expiry_date - now_utc).days
        
        print(f"Domain: {domain}")
        print(f"SSL Expiration Date: {expiry_date}")
        print(f"Days Remaining: {remaining_days}")
        
        logging.info(f"{domain} SSL expires on {expiry_date}. Days left: {remaining_days}")
        
        if remaining_days < 30:
            print("⚠️ Warning: SSL certificate expires soon!")
            send_email_alert(domain, expiry_date, remaining_days)
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
