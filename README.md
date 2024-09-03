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
    git clone https://github.com/PriyanshuLathi/Face-Tracking-Robotic-Arm
    ```

2. Install the required Python dependencies.

3. Upload the Arduino sketch (`face_tracking_robotic_arm_arduino.ino`) to your Arduino board using the Arduino IDE.

## Usage:
1. Connect the Arduino board to your computer via USB cable.
2. Run the Python script `Face_following_2.py`:

    ```bash
    python Face_following_2.py
    ```

3. Position the robotic arm in front of the camera, ensuring it has a clear view of the surroundings.
4. The robotic arm will start tracking and following detected faces in real-time.

## Configuration:
- Adjust the `SERVO_PIN` and `CAMERA_INDEX` variables in the `Face_following_2.py` script according to your setup.
- Fine-tune the `SPEED` and `SENSITIVITY` parameters to achieve optimal performance based on your environment and requirements.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/PriyanshuLathi/Face-Tracking-Robotic-Arm/blob/main/LICENSE) file for details.

## Contact

For questions or feedback, feel free to reach out:

- LinkedIn: [Priyanshu Lathi](https://www.linkedin.com/in/priyanshu-lathi)
- GitHub: [Priyanshu Lathi](https://github.com/PriyanshuLathi)

## Authors
- Priyanshu Lathi