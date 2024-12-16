# Sending an Email with Attachments
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Email Credentials
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"

# Email Content
subject = "Email with Attachment"
body = "Please find the attachment."
receiver = "receiver_email@example.com"
attachment_path = "example.pdf"  # Path to your file

# Create Email
msg = MIMEMultipart()
msg["From"] = EMAIL_ADDRESS
msg["To"] = receiver
msg["Subject"] = subject

# Attach Body
msg.attach(MIMEText(body, "plain"))

# Attach File
with open(attachment_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={attachment_path}")
    msg.attach(part)

# Send the Email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print("Email with attachment sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
