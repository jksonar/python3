# Sending HTML Emails
import smtplib
from email.mime.text import MIMEText

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Email Credentials
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"

# Email Content
subject = "HTML Email"
html_body = """
<html>
  <body>
    <h1>Welcome to Python SMTP</h1>
    <p>This is an <b>HTML</b> email!</p>
  </body>
</html>
"""
receiver = "receiver_email@example.com"

# Create Email
msg = MIMEText(html_body, "html")
msg["From"] = EMAIL_ADDRESS
msg["To"] = receiver
msg["Subject"] = subject

# Send the Email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print("HTML Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
