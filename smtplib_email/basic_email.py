# 1. Basic Setup to Send Email
import smtplib
from email.mime.text import MIMEText

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"  # Example: Gmail SMTP server
SMTP_PORT = 587                 # TLS Port

# Email Credentials
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"

# Email Content
subject = "Test Email"
body = "This is a test email sent from Python."
receiver = "receiver_email@example.com"

# Create the Email
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = EMAIL_ADDRESS
msg["To"] = receiver

# Send the Email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Upgrade connection to secure
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
