import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert():
    sender_email = "23105086@usc.edu.ph"
    receiver_email = "anythingtech86@gmail.com"
    app_password = "qolcreimaoseqcvl"  # 16-character Gmail App Password

    subject = "🔥 FIRE DETECTED ALERT"
    body = "Emergency: A fire has been detected by your system. Please check the area immediately."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("🚨 Fire alert email sent to anythingtech86@gmail.com!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
    finally:
        server.quit()

# Dummy fire detection loop
while True:
    input_value = input("Enter 1 for FIRE DETECTED, 0 for no fire, or 'exit' to quit: ")

    if input_value == "1":
        print("🔥 FIRE DETECTED!")
        send_email_alert()
    elif input_value == "0":
        print("✅ No fire detected.")
    elif input_value.lower() == "exit":
        print("👋 Exiting program.")
        break
    else:
        print("⚠️ Invalid input. Please enter 1, 0, or 'exit'.")
