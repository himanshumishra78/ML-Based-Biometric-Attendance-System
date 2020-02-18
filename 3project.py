import face_recognition
import cv2
import numpy as np
import pandas as pd
import time

video_capture = cv2.VideoCapture(0)


while True:
    ret, frame = video_capture.read()
    cv2.imshow('frame',frame)
    k=cv2.waitKey(0)
    if(k=='q'):
        cv2.destroyAllWindow()
        
