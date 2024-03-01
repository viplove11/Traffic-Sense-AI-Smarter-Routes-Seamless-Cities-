# Object Detection with Arduino Traffic Light Control

This project utilizes YOLO (You Only Look Once) object detection model to detect objects in real-time using a webcam feed. The detected object count is then sent to an Arduino Uno board via serial communication, which controls a simulated traffic light system based on the number of detected objects.

## Prerequisites

Before running the project, make sure you have the following dependencies installed:

- Python 3
- OpenCV
- Pandas
- Numpy
- Ultralytics YOLO library
- Arduino IDE (for uploading the code to Arduino board)

## Setup

1. Clone the repository to your local machine: git clone <repository_url>
2. Connect the Arduino Uno board to your computer via USB.
3. Install the required Python dependencies using pip: pip install -r requirements.txt
4. Upload the `object_detect_arduino/object_detect_arduino.ino` file to your Arduino Uno board using the Arduino IDE.
5. Adjust the `COM` port in the Python script (`FinalTest.py`) to match the port to which your Arduino Uno is connected.

## Usage

1. Run the Python script `FinalTest.py`:

2. The script will open a webcam feed displaying the real-time object detection. The detected object count will be sent to the Arduino Uno board, which will control the simulated traffic lights accordingly.

3. To exit the program, press `Esc` key.

## Arduino Code Explanation

The Arduino code (`object_detect_arduino.ino`) listens for input from the serial port and controls the LEDs connected to pins `10` (Red), `11` (Yellow), and `12` (Green) based on the received input. Here's a brief explanation of the code:

- The `setup` function initializes serial communication with a baud rate of `9600` and sets the pin modes for the LEDs.

- The `loop` function continuously reads data from the serial port. Based on the received value (`1`, `2`, or `3`), it turns on the respective LED:
  - `1`: Red LED on, others off.
  - `2`: Yellow LED on, others off.
  - `3`: Green LED on, others off.