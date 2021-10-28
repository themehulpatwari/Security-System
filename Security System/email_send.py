# For future refference(Python Tutorial) https://www.youtube.com/watch?v=JRCJ6RtE3xU

import os
import smtplib
import imghdr
from email.message import EmailMessage

def send_email(email_name, file_name):
    # Environment Variable containing email and password
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # Body of the email
    msg = EmailMessage()
    msg['Subject'] = 'Urgent Security Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email_name
    msg.set_content('''Movement Detected on Camera.
    Constant Video of the Intruder is currently being saved on the device.
    The image is attached below.''')

    # Reading the file
    with open(file_name, 'rb') as f:
        file_data = f.read()

    # Adding the file as an attatchment.
    msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)

    # Sending the mail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

        smtp.send_message(msg)


