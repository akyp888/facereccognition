import os
import face_recognition
import cv2
video_capture = cv2.VideoCapture(0)

dirListing = os.listdir("faces")
known_face_names = []
known_face_encodings = []
i=0
for item in dirListing:
        known_face_encodings.append(item.strip("[.jpg]")+"_face_encoding")
        path="faces/"+item
        known_face_encodings[i] = face_recognition.face_encodings(face_recognition.load_image_file(path))[0]
        i=i+1
        known_face_names.append(item.strip("[.jpg]"))
