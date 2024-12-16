# Sending to Multiple Recipients
import smtplib
from email.mime.text import MIMEText

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Email Credentials
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"

# Email Content
subject = "Email to Multiple Recipients"
body = "This email is sent to multiple recipients."
receivers = ["recipient1@example.com", "recipient2@example.com"]

# Create Email
msg = MIMEText(body)
msg["From"] = EMAIL_ADDRESS
msg["To"] = ", ".join(receivers)
msg["Subject"] = subject

# Send the Email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, receivers, msg.as_string())
        print("Email sent to multiple recipients!")
except Exception as e:
    print(f"Failed to send email: {e}")
