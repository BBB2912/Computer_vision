import os
import cv2
import numpy as np

'''firstly we can read all images from folder and convert into grayscale and save croped faces as features 
and labela as men and women'''
genders=['male','female']  #these are the categores we want predict
dir=r'C:\Users\MAHIREDDY\OneDrive\Pictures\gender_recognition'   #this the directory path saveas raw string to avoid escape sequences
harcascade=cv2.CascadeClassifier('harcascades.xml')     #this the file provide face example cordinates for comparing
faces=[]
gender=[]
def creat_train():
    ''' acces folder by using os module and join dir path and name as men and women and enter into that
    and label set as male first iteration female for second iteration'''
    for i,cat in enumerate(['men','women']):
        path=os.path.join(dir,cat)
        label=i
        ''' now afetr enter into the folder read ach img using os module by jin previous generating path
        and img name'''
        for img in os.listdir(path):
            img_read=os.path.join(path,img)
            img_array=cv2.imread(img_read)
            '''convert bgr format img into grayscale img beacause colors or avoid by model in
            the time of edge detection'''
            gray=cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)
            '''now detect face using detectMultiscale method'''
            face_rect=harcascade.detectMultiScale(gray,1.1,8)

            '''now wecan crop that face by given cordinates by face-rect'''
            for (x,y,w,h) in face_rect:
                face_roi=gray[y:y+h,x:x+w] #this the cropped image
                faces.append(face_roi)
                gender.append(label)
creat_train()
print('trainign done............')

'''now convert that faces and genders into  arrays objects'''
faces=np.array(faces,dtype='object')
gender=np.array(gender)

'''create object for LBPHFaceRecognizer model'''
gender_recognizer=cv2.face.LBPHFaceRecognizer_create()

'''train this model now'''
gender_recognizer.train(faces,gender)

'''save this entire model in yml file'''
gender_recognizer.save('gender_recognize.yml')

'''save the faces and gender file also'''
np.save('faces.npy',faces)
np.save('gender.npy',gender)

