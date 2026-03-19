import smtplib
from email.mime.text import MIMEText
from config import EMAIL_CONFIG

def send_email_alert(message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = 'System Alert'
        msg['From'] = EMAIL_CONFIG["sender"]
        msg['To'] = EMAIL_CONFIG["receiver"]

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(EMAIL_CONFIG["sender"], EMAIL_CONFIG["password"])
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print("Email failed:", e)
