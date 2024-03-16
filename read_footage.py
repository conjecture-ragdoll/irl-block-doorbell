import numpy as np
import os
import cv2
from deepface import DeepFace

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
        for detector in detectors:
            face = DeepFace.detectFace(frame_photo, detector_backend = detector)
            return face
    except:
        pass

def identifyFace(frame_photo, path_to_contact_photos):
    '''
    Identifies face by showing the directory under Contacts
    '''
    contact_list = os.listdir(path='./Contacts')
    try:
        for contact in contact_list:
            for detector in detectors:
                face = DeepFace.find(img_path=frame_photo, db_path=f'./Contacts/', detector_backend=detector)
            
                return face['identity']
                    
                
                    '''
                    if user selects acceptingNewVisitors as True create new contact
                    '''
            
    except:
        pass        

cap = cv2.VideoCapture("footage/vid0.mp4")  # 0 represents the default camera (Raspberry Pi Camera Module)

while cap.isOpened():
    # Read a frame from the video capture
    ret, frame = cap.read()
    # Check if the frame is read successfully
    if not ret:
        print("Error: Could not read frame.")
        break
   
    cv2.imwrite('footage/temp.png', frame)
    if findFace('footage/temp.png'):
    identifyFace('footage.temp.png', './Contacts')
    
# Release the video capture object and close the OpenCV window
cap.release()

