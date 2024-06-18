import cv2
import numpy as np
import winsound
video=cv2.VideoCapture(0)
eye_cascade=cv2.CascadeClassifier(r'C:\Users\MAHIREDDY\OneDrive\Desktop\computer_vision\opencv\harcascades\harcascade_eye_tree_glassless.xml')
while True:
    _,frame=video.read()
    eye_roi=eye_cascade.detectMultiScale(frame,1.3,5,minSize=(50,50))
    if len(eye_roi) == 0:
        print(len(eye_roi))
        winsound.Beep(500,300)
    if cv2.waitKey(1)==ord('d'):
        break
    cv2.imshow('eydeted',frame)
video.release()
cv2.destroyAllWindows()