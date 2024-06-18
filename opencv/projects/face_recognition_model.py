import os
import cv2
import numpy as np
people=['mahireddy','rabbit','sumanth']
dir=r'opencv/images'
harcascade=cv2.CascadeClassifier('harcascades.xml')
features=[]
labels=[]
def create_train():
    for person in people:
        path=os.path.join(dir,person)
        label=people.index(person)
        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv2.imread(img_path)
            gray=cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)

            face_rect=harcascade.detectMultiScale(gray,1.1,4)
            for (x,y,w,h) in face_rect:
                face_roi=gray[y:y+h,x:x+w]
                features.append(face_roi)
                labels.append(label)
create_train()
print('taining done..........')

features=np.array(features,dtype='object')
labels=np.array(labels)
face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)
