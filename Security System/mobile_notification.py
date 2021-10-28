import os
from pushbullet import Pushbullet

def send_notification():
    # API Key for Pushbullet Notification
    API_KEY = os.environ.get("NOTIFICATION_API")
    file = 'push_notification.txt'

    # Reading the text file.
    with open(file, mode = 'r') as f:
        text = f.read()

    try:
        # Sending the notification
        pb = Pushbullet(API_KEY)
        # pb.push_note(Title for Notification, Body for Notification)
        push = pb.push_note('URGENT SECURITY ALERT', text)
    except:
        print('Internet not available, notification not sent')

