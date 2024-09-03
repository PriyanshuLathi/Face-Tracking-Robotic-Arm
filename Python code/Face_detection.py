import cv2
import numpy as np
import time

face_classifier = cv2.CascadeClassifier("D:\FACE_TRACKING\haarcascade_frontalface_default.xml")

video_cam = cv2.VideoCapture(0)

if not video_cam.isOpened():
    print("Camera cannot be accessed")
    exit()

q_key_pressed = False
while (q_key_pressed == False):
    ret, frame = video_cam.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # print("Number of faces detected: ", len(faces))
        text = "Number of Faces Detected = " + str(len(faces))

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, text, (0, 30), font, 1, (255, 0, 0), 1)

        cv2.imshow("Result", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            q_key_pressed = True
            break

video_cam.release()
cv2.destroyAllWindows()