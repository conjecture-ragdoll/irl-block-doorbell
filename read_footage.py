import numpy as np
import os
import cv2
from deepface import Deepface

print(cv2.__version__)

detectors = [
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

def acceptingNewVisitors(boolean):
    return boolean

def nameAlreadyExists(nameOfContact, path_to_contacts):
    return os.path.isdir(f'Contacts/{nameOfContact}')

def confirmSame(nameOfContact, face_image):
    '''
    If user inputs a name already in Contacts
    '''
    feedback_dialogue = f'Is {nameOfContact} the same person as: '
    pass    

def createContact(nameOfContact, face_image):
    '''
    Create a directory and add image of face
    '''
    feedback_dialogue = "Add to contacts?"
    pass

def findFace(frame_photo):
    '''
    TODO: detect multiple faces
    '''
    try:
        for detector in enumerate(detectors):
            face = DeepFace.detectFaces(frame_photo, detector_backend = detector)
            return face
    except:
        pass

def identifyFace(frame_photo, path_to_contact_photos):
    '''
    Identifies face by showing the directory under Contacts
    '''
    try:
        for detector in enumerate(detectors):
            face = DeepFace.verify(img_path=frame_photo, db_path=path_to_contact_photos, detector_backend=detector)
            
            if face['verified']:
                return os.listdir('.')
            
            else:
                '''
                if user selects acceptingNewVisitors as True create new contact
                '''
                pass
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
    identifyFace('footage.temp.png', './Contacts')
    
# Release the video capture object and close the OpenCV window
cap.release()

