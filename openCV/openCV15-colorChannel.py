import cv2
import numpy as np
print(cv2.__version__)


dispW=640
dispH=480
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)



blank = np.zeros([480,640,1],np.uint8)



#cam=cv2.VideoCapture(1)
while True:
     ret, frame=cam.read()
     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     #print(gray.shape)
     #print(gray.size)
     print(frame[50,45,1]) # print the green value on the pixel on the 50th row (down) and 45th column (across)
     #b=cv2.split(frame)[0]
     #g=cv2.split(frame)[1]
     #r=cv2.split(frame)[2]
     b,g,r=cv2.split(frame) 
     
     b=cv2.merge((b,blank,blank))
     g=cv2.merge((blank,g,blank))
     r=cv2.merge((blank,blank,r))


     cv2.imshow('piCam',frame)
     cv2.moveWindow('piCam',0,0)
     cv2.imshow('b',b)
     cv2.moveWindow('b',dispW,0)

     cv2.imshow('g',g)
     cv2.moveWindow('g',dispW*2,0)

     cv2.imshow('r',r)
     cv2.moveWindow('r',dispW*3,0)

     cv2.imshow('blank',blank)
     cv2.moveWindow('blank',0,dispH)






     if cv2.waitKey(1)==ord('q'):
         break
cam.release()
cv2.destroyAllWindows()