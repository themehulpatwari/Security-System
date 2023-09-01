# Security-System
Security System using OpenCV

Files in this Repository:
1. email_send.py - This file contains python code to send an email when something is detected on the camera.
2. mobile_notification.py - This file sends a notification to the devices you have connected with the help of Pushbullet.
3. push_notification.txt - Text file which contains the body of the notification.
4. main.py - This is the main project file. When a body or face is detected then it automatically starts recording the video and it also sends a notification and an email which contains a photo of the face detected. The email can only be sent once every hour if something is detected, because we don't want the user getting tons of notification and email.


Prerequisites:
1. Modules which need to be downloaded - SMTPLIB (for email), Pushbullet (for notifications), OpenCV (cv2 for body, face detectiom and camera interface)
