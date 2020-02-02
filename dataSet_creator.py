import cv2
import numpy as np
import trainer
from tkinter import messagebox
from tkinter import simpledialog
import database
def main():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam=cv2.VideoCapture(0)
    id=simpledialog.askstring("userid","Enter the userid:")
    name=simpledialog.askstring("username","Enter the userName:")
    database.insert_name(id,name)
    
    sampleNum=0
    while(True):
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.5,2)
        print(faces)
        for(x,y,w,h) in faces:
            sampleNum+=1
            cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            
            cv2.waitKey(100)
        cv2.imshow("Face",img)
        cv2.waitKey(1)
        if(sampleNum>20):
            break
        
    cam.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("info","User is Registered.Thank you for joining us")
    trainer.main()
