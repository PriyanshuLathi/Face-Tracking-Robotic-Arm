

# Face Tracking Robotic Arm

## Introduction:
This project is a face tracking robotic arm developed using OpenCV, Arduino, and PyFirmata. The purpose of this project is to demonstrate how computer vision techniques can be integrated with robotics to create an interactive system capable of tracking and following human faces in real-time.

## Features:
- Real-time face detection and tracking using OpenCV.
- Control of a robotic arm using Arduino and PyFirmata.
- Smooth and precise movement of the robotic arm to follow detected faces.
- Adjustable parameters for sensitivity and speed of the robotic arm movement.
- Simple and intuitive interface.

## Requirements:
- Python 3.2
- OpenCV
- PyFirmata
- Arduino board (e.g., Arduino Uno)
- Robotic arm kit
- USB cable

## Installation:
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/face-tracking-robotic-arm.git
    ```

2. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Upload the Arduino sketch (`arduino_face_tracking.ino`) to your Arduino board using the Arduino IDE.

## Usage:
1. Connect the Arduino board to your computer via USB cable.
2. Run the Python script `face_tracking.py`:

    ```bash
    python face_tracking.py
    ```

3. Position the robotic arm in front of the camera, ensuring it has a clear view of the surroundings.
4. The robotic arm will start tracking and following detected faces in real-time.

## Configuration:
- Adjust the `SERVO_PIN` and `CAMERA_INDEX` variables in the `face_tracking.py` script according to your setup.
- Fine-tune the `SPEED` and `SENSITIVITY` parameters to achieve optimal performance based on your environment and requirements.

## Author
- Priyanshu Lathi