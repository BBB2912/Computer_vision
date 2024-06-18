import numpy as np
import cv2

harcascade=cv2.CascadeClassifier('harcascades.xml')
people=['mahireddy','rabbit']
features=np.load('features.npy',allow_pickle=True)
labels=np.load('labels.npy')

face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

vedio=cv2.VideoCapture(0)
while True:
    istrue,frame=vedio.read()
    frame=cv2.resize(frame,(500,500),interpolation=cv2.INTER_AREA)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face_rct=harcascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in face_rct:
        fce_roi=gray[y:y+h,x:x+w]
        label,confidence=face_recognizer.predict(fce_roi)
        print(f'{people[label]} with confidence of {confidence} ')
        cv2.putText(frame,people[label],(x-10,y-10),cv2.FONT_ITALIC,1,(255,0,0),5)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('destination',frame)
    if cv2.waitKey(1)==ord('d'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
