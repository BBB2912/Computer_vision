import cv2
import numpy as np

video=cv2.VideoCapture(0)
eye_cascade=cv2.CascadeClassifier('harcascade_eye.xml')
while True:
    _,frame=video.read()
    bilate=cv2.bilateralFilter(frame,11,3,3)
    cv2.imshow('bilate',bilate)
    eye_roi=eye_cascade.detectMultiScale(frame,1.3,5,minSize=(50,50))
    for (x,y,w,h) in eye_roi:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    if cv2.waitKey(1)==ord('d'):
        break
    cv2.imshow('eydeted',frame)
video.release()
cv2.destroyAllWindows()