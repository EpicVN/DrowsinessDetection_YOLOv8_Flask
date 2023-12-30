Drowsiness Detection

## Description
The project is a proof of concept application developed using the Flask library. It utilizes the YOLOv8 machine learning algorithm for object detection, specifically targeting the identification of humans and vehicles trespassing in forest areas. The purpose of the project is to assist forest authorities in efficiently dealing with trespassing incidents without the need for constant patrolling, thereby optimizing resource utilization.

## Features
### Object Detection: The application utilizes the trained YOLOv8 model to detect drowsiness face in real-time using the webcam feed.
### Custom Dataset: The model has been trained on a custom dataset specific to drowsiness face.
### Flask Web Application: The project is implemented as a Flask web application.

## Installation
1. Clone the project repository:
 `git clone`
 
2. Install the required dependencies:
 `pip install -r requirements.txt`
 
## Usage
1. Start the Flask application:
 `python flaskapp.py`
 
2. Access the application through the provided URL (e.g., http://localhost:5000).

3. Grant necessary permissions to access the webcam.

4. Once the webcam feed is displayed, the application will automatically detect and highlight drowsiness face in the video stream.

5. You can also upload video and image to detect instead
