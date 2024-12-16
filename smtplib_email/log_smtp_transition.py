#  Logging SMTP Transactions
import smtplib
import logging
from email.mime.text import MIMEText

# Setup Logging
logging.basicConfig(level=logging.DEBUG)

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"

# Email Content
subject = "Logging SMTP Transactions"
body = "This email logs SMTP transactions."
receiver = "receiver_email@example.com"

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = EMAIL_ADDRESS
msg["To"] = receiver

# Send Email with Logging
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.set_debuglevel(1)  # Enable debug output
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print("Email sent successfully with logs!")
except Exception as e:
    print(f"Failed to send email: {e}")
