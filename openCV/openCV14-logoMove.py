import cv2
import numpy as np
print(cv2.__version__)

dispW=640
dispH=480
flip=2
plLogoSize = 5 #1/x of the frame

plLogo = cv2.imread('pl.jpg')
plLogo = cv2.resize(plLogo,(int(dispH/plLogoSize),int(dispH/plLogoSize)))
plLogoGray = cv2.cvtColor(plLogo,cv2.COLOR_BGR2GRAY)
_,plBGMask = cv2.threshold(plLogoGray,220,255,cv2.THRESH_BINARY)
plFGMask = cv2.bitwise_not(plBGMask)
plFG = cv2.bitwise_and(plLogo,plLogo,mask=plFGMask)

cv2.imshow('plLogo',plLogo)
cv2.moveWindow('plLogo',dispW+55,0)

cv2.imshow('plLogoGray',plLogoGray)
cv2.moveWindow('plLogoGray',int(dispW+55+(dispW/plLogoSize)*1),0)

cv2.imshow('plBGMask',plBGMask)
cv2.moveWindow('plBGMask',int(dispW+55+(dispW/plLogoSize)*2),0)

cv2.imshow('plFGMask',plFGMask)
cv2.moveWindow('plFGMask',int(dispW+55+(dispW/plLogoSize)*3),0)

cv2.imshow('plFG',plFG)
cv2.moveWindow('plFG',int(dispW+55+(dispW/plLogoSize)*4),0)

#___________
xState=1
yState=1
x=1
y=1
speed=2


camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(1)
while True:
     ret, frame=cam.read()
     
     if xState == 1: 
         x=x+speed
         if x >= dispW-dispH/plLogoSize:
             xState = 2
     if xState == 2:
         x=x-speed
         if x <= 0:
             xState =1
     
     if yState == 1: 
         y=y+speed
         if y >= dispH-dispH/plLogoSize:
             yState = 2
     if yState == 2:
         y=y-speed
         if y <= 0:
             yState =1
     
     ROI = frame[y:y+int(dispH/plLogoSize),x:x+int(dispH/plLogoSize)]
     ROI = cv2.bitwise_and(ROI,ROI,mask=plBGMask)
     ROI = cv2.add(ROI,plFG)
     
     cv2.imshow('ROI',ROI)
     cv2.moveWindow('ROI',int(dispW+55+(dispW/plLogoSize)*5),0)

     frame[y:y+int(dispH/plLogoSize),x:x+int(dispH/plLogoSize)] = ROI
     

       
     
     
     cv2.imshow('piCam',frame)
     cv2.moveWindow('piCam',0,0)

     if cv2.waitKey(1)==ord('q'):
         break
cam.release()
cv2.destroyAllWindows()