import cv2
import numpy as np
print(cv2.__version__)


dispW=640
dispH=480

flip=2
boxSize = 300

img1=np.zeros((dispH,dispW,1),np.uint8) # make a matrix of zeros, with 1 value per cell (because we want a black/white image), select the datatype: numpy unsigned integer 8 bits
img1[0:480,0:320]=[255]

img2=np.zeros((480,640,1),np.uint8)
img2[int(dispH/2-boxSize/2):int(dispH/2+boxSize/2),int(dispW/2-boxSize/2):int(dispW/2+boxSize/2)]=[255]

bitAnd=cv2.bitwise_and(img1,img2)
bitOr = cv2.bitwise_or(img1,img2)
bitXor = cv2.bitwise_xor(img1,img2) # exclusive or : one OR another, not both
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(1)
while True:
     ret, frame=cam.read()
     
     cv2.imshow('piCam',frame)
     cv2.moveWindow('piCam',0,0)

     cv2.imshow('img1',img1)
     cv2.moveWindow('img1',0,dispH+55)

     cv2.imshow('img2',img2)
     cv2.moveWindow('img2',dispW+70,0)

     cv2.imshow('AND', bitAnd)
     cv2.moveWindow('AND',dispW+70,dispH+55)

     cv2.imshow('OR', bitOr)
     cv2.moveWindow('OR',dispW*2+70,0)

     cv2.imshow('XOR', bitXor)
     cv2.moveWindow('XOR',dispW*2+70,dispH+55)

     frameXor=cv2.bitwise_and(frame,frame,mask=bitXor) #you're only combining 1 image not 2 but there are 2 function inputs, so you list 'frame' twice (not super important)

     cv2.imshow('XOR Mask', frameXor)
     cv2.moveWindow('XOR Mask',dispW*3+70,0)

     if cv2.waitKey(1)==ord('q'):
         break
cam.release()

cv2.destroyAllWindows()