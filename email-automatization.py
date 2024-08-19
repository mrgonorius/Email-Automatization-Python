import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_daily_email():
    sender_email = "your_email@example.com"
    receiver_email = "recipient_email@example.com"
    password = "your_password"

    # Create the email content
    message = MIMEMultipart("alternative")
    message["Subject"] = "Daily Report"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Email body
    body = "This is your daily report."
    part1 = MIMEText(body, "plain")
    message.attach(part1)

    # Send the email
    try:
        with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

# Schedule the email to be sent daily at midnight
schedule.every().day.at("00:00").do(send_daily_email)

while True:
    schedule.run_pending()
    time.sleep(60)