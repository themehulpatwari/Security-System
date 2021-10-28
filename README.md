# Security-System
Security System using OpenCV

Files in this Repository:
1. email_send.py - This file contains python code to send an email when something is detected on the camera.
2. mobile_notification.py - This file sends a notification to the devices you have connected with the help of Pushbullet.
3. push_notification.txt - Text file which contains the body of the notification.
4. main.py - This is the main project file. When a body or face is detected then it automatically starts recording the video and it also sends a notification and an email which contains a photo of the face detected. The email can only be sent once every hour if something is detected, because we don't want the user getting tons of notification and email.


Prerequisites:
1. Modules which need to be downloaded - SMTPLIB (for email), Pushbullet (for notifications), OpenCV (cv2 for body, face detectiom and camera interface)

Useful Links :
1. Sending an email with python: https://www.youtube.com/watch?v=JRCJ6RtE3xU&t=1522s
2. I have used local environment variable which contains the information regarding my email, password and api token for pushbullet. I used it so that I don't have to write my credentials. I will attach a link which contains information about creating environment variables.
Environment Variables (Windows): https://www.youtube.com/watch?v=IolxqkL7cD8
Environment Variables (Mac and linux): https://www.youtube.com/watch?v=5iWhQWVXosU&t=78s
3. Open CV Security Camera: https://www.youtube.com/watch?v=Exic9E5rNok
4. Sending Notification: https://www.youtube.com/watch?v=tbzPcKRZlHg
