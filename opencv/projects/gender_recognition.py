import cv2
import numpy as np

harcascade=cv2.CascadeClassifier('harcascades.xml')
genders=['male','female']
# faces=np.load('faces.npy',allow_pickle=True)
# gender=np.load('gender.npy')

gender_recognizer=cv2.face.LBPHFaceRecognizer_create()
gender_recognizer.read('gender_recognize.yml')

# img=cv2.imread(r'C:\Users\MAHIREDDY\OneDrive\Pictures\gender_recognition\women\w5.jpeg')
video=cv2.VideoCapture(0)
while True:
    istrue,img=video.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face_rect=harcascade.detectMultiScale(gray,1.05,6)

    for (x,y,w,h) in face_rect:
        face_roi=gray[y:y+h,x:x+w]
        '''now we can predict this face is male or female '''
        gende,confidece=gender_recognizer.predict(face_roi)

        print(f'{genders[gende]} with confidence of {confidece}')

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3,cv2.LINE_AA)
        cv2.putText(img,genders[gende].capitalize(),(x,y-4),cv2.FONT_ITALIC,1,(255,0,255),2)
    img=cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)
    cv2.imshow('genderimg',img)
    if cv2.waitKey(1)==ord('d'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()

