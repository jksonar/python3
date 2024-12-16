# Using SSL for Secure Email
import smtplib
from email.mime.text import MIMEText

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # SSL Port

# Email Credentials
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"

# Email Content
subject = "Secure Email with SSL"
body = "This email is sent over SSL."
receiver = "receiver_email@example.com"

# Create Email
msg = MIMEText(body)
msg["From"] = EMAIL_ADDRESS
msg["To"] = receiver
msg["Subject"] = subject

# Send the Email
try:
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print("Secure Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
