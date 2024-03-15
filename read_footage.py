import numpy as np
import cv2
from deepface import Deepface

print(cv2.__version__)

detectors = models = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace", 
  "DeepFace", 
  "DeepID", 
  "ArcFace", 
  "Dlib", 
  "SFace",
]



# Open a video capture object for the Raspberry Pi camera
cap = cv2.VideoCapture("footage/vid0.mp4")  # 0 represents the default camera (Raspberry Pi Camera Module)

def findFace(frame_photo):
    '''
    TODO: detect multiple faces
    '''
    try:
        for detector in enumerate(detectors):
            face = DeepFace.detectFaces(frame_photo, detector_backend = detector)
    except:
        pass

def identifyName(frame_photo, path_to_contact_photos):
    try:
        for detector in enumerate(detectors):
            face = DeepFace.verify(img_path=frame_photo, db_path=path_to_contact_photos, detector_backend=detector)
        # Display name of face
            print(face)
    except:
        pass        

while cap.isOpened():
    # Read a frame from the video capture
    ret, frame = cap.read()
    # Check if the frame is read successfully
    if not ret:
        print("Error: Could not read frame.")
        break
   
    cv2.imwrite('footage/temp.png', frame)
    identifyName('footage.temp.png', './Contacts')
    
# Release the video capture object and close the OpenCV window
cap.release()

