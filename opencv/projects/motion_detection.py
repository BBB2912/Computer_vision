import cv2
import numpy as np
import winsound

video=cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH,640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
while True:
    _,frame1=video.read()
    _,frame2=video.read()
    diff=cv2.absdiff(frame1,frame2)
    gray_diff=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur_diff=cv2.GaussianBlur(gray_diff,(5,5),0)
    threshhold,thresh=cv2.threshold(blur_diff,30,255,cv2.THRESH_BINARY)
    dialate=cv2.dilate(thresh,None,iterations=3)
    contoures,_=cv2.findContours(dialate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contoures:
        if cv2.contourArea(cnt)<2000:
            continue
        x,y,w,h=cv2.boundingRect(cnt)

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),3)
        winsound.Beep(500, 200)
    if cv2.waitKey(30)==ord('d'):
        break

    cv2.imshow('motion_window',frame1)
    cv2.imshow('w', dialate)
video.release()
cv2.destroyAllWindows()