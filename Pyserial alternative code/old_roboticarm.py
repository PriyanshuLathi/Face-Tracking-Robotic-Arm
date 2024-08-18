import numpy as np
import serial
import time
import sys
import cv2


arduino = serial.Serial('COM5', 9600)
time.sleep(2)
print("Connected to Arduino...")


face_cascade = cv2.CascadeClassifier('D:/Robotic_arm/.venv/Lib/site-packages/opencv_python-4.9.0.80.dist-info/haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0ncv)


cv2.namedWindow('img', cv2.WINDOW_NORMAL)  # Create a resizable window

# Read the captured image, convert it to Gray image and find faces
while True:
    ret, img = cap.read()
    cv2.line(img, (500, 250), (0, 250), (0, 255, 0), 1)
    cv2.line(img, (250, 0), (250, 500), (0, 255, 0), 1)
    cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3)

    # Detect the face and make a rectangle around it.
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        # Center of the ROI (Rectangle)
        xx = int(x + (x + h)) // 2
        yy = int(y + (y + w)) // 2
        center = (xx, yy)

        # Sending data to Arduino
        print("Center of Rectangle is :", center)
        data = "X{0:d}Y{1:d}Z".format(xx, yy)
        print("Output = '" + data + "'")
        arduino.write(data.encode())

    # Display the stream.
    cv2.imshow('img', img)

    # Resize the window
    cv2.resizeWindow('img', 500, 500)

    # Hit 'Esc' to terminate execution
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()



