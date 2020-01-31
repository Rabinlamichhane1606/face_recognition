import cv2
import dataSet_creator
def main():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam=cv2.VideoCapture(0)
    rec=cv2.face.LBPHFaceRecognizer_create()
    rec.read('recognizer\\trainingData.yml')
    
    font=cv2.FONT_HERSHEY_SIMPLEX
    while(True):
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,2)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            if(id==1):
                id="Rabin"
            elif(id==2):
                id="Ranjan"
            elif(id==3):
                id="Anmol"
            elif(id==4):
                id="Sanjiv"
            else:
                id="guest"
            cv2.putText(img,str(id),(x,y+h), font, 1,(190,200,125),2,cv2.LINE_AA)
        cv2.imshow("Face",img)
        
        if(cv2.waitKey(1))==ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()





