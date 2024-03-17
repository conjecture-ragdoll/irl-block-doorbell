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

acceptingNewVisitors = True

def acceptingNewVisitors(boolean):
    acceptingNewVisitors = boolean

def addToPhotos(contactDir, face_image):
    '''
    contactDir is name of Contact folder containing the images
    '''

    '''
    In case of duplicate images, format string of path in the directory
    '''
    countTotal = len(os.listdir(os.path.join('Contacts', contactDir)))
    cv2.imwrite(os.path.join('Contacts', contactDir, f'{contactDir}%d' % countTotal), face_image)

def YNFeedback(feedback_input):
    '''
    Ask in y/n format
    '''
    feedback_dialogue = input(feedback_input)
    feedback = feedback_dialogue.lower()
    return feedback in ['y', 'yes']

def nameAlreadyExists(nameOfContact):
    return nameOfContact in os.path.isdir('./Contacts')
        
def addToContactDir(nameOfContact, face_image):
    if nameAlreadyExists(nameOfContact):
        if YNFeedback(f'Are they the same person? A {nameOfContact} already exists?\nPlease Enter y/n: '):
            if YNFeedback(f'Are you sure {nameOfContact} is the same person? y/n: '):
                addToPhotos(nameOfContact, face_image)   
    else:
        newContactDir = os.mkdir(os.path.join('Contacts', nameOfContact))    
        addToPhotos(newContactDir, face_image)

def cropFaces(frame_photo):
    '''
    TODO: detect multiple faces
    '''
    try:
        for detector in detectors:
            face_objs = DeepFace.extract_faces(frame_photo, detector_backend = detector)
            return face_objs
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
    
    try:
        if acceptingNewVisitors:
            if cropFaces('footage/temp.png'):
                print(identifyFace('footage.temp.png', './Contacts'))

        else:
            pass
                        
    except:
        pass
# Release the video capture object and close the OpenCV window
cap.release()

