import numpy as np
import cv2

# print(cv2.__version__)



# Open a video capture object for the Raspberry Pi camera
cap = cv2.VideoCapture("footage/vid0.mp4")  # 0 represents the default camera (Raspberry Pi Camera Module)

# Set the camera resolution (adjust as needed)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open Raspberry Pi camera.")
    exit()

# Read and display video frames until the user presses the 'q' key
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the frame
    cv2.imshow('Raspberry Pi Camera', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()

