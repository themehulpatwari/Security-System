import cv2
import time
import datetime
import mobile_notification
from pushbullet import Pushbullet
from email_send import send_email
from mobile_notification import send_notification

# Video Capture Device
cap = cv2.VideoCapture(0)

# Detecting Face and Body using Open Cv Cascade Classifiers.
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

# Screen Display Size
frame_size = (int(cap.get(3)), int(cap.get(4)))
# Video Format for saving video.
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

HOUR = []

while True:
    _ , frame = cap.read()

    # Converting Video to Gray Scale for open cv face detection to work.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detecting whether any face or a body is present or not.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            # Starting the recording and capturing an image.
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            cv2.imwrite(f"{current_time}.png", frame)
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
            print('Started Recording')
    elif detection:
        # If the detection is stopped, then a timer is started to record after a certain period of time.
        # If the face or body becomes visible then the recording goes on but if it is not detected,
        # for certain period of time then the recording stops.

        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print('Stop Recording')

                # This block of code ensures that only one email and notification is being sent per hour
                # to the user if any face is detected because you don't want the user getting too many email.
                # An image is sent to the email if face or body is detected.
                # I have used try and except incase, no Internet is available.
                HOUR.append(datetime.datetime.now().strftime("%d-%m-%Y-%H"))
                try:
                    if len(HOUR) == 1:
                        send_email('youremailid@xyz.com', f"{current_time}.png")
                        send_notification()
                    elif HOUR[-1] != HOUR[-2]:
                        send_email('youremailid@xyz.com', f"{current_time}.png")
                        send_notification()
                except:
                    print('No Wifi Available.')
                if len(HOUR) == 3:
                    HOUR = [HOUR[-2], HOUR[-1]]

        else:
            timer_started = True
            detection_stopped_time = time.time()

    # Displaying the camera on screen.
    if detection:
        out.write(frame)
    # Drawing rectangle around faces on screen.
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    cv2.imshow("Camera", frame)

    # Exiting the camera screen.
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
