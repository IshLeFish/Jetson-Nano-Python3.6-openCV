import cv2
print(cv2.__version__)


dispW=640
dispH=480
flip=0

#draw a rectangle on the screen. the following setting changes the rectangle from center-controlled to corner-controlled
    #rectangleType:
        #1: corner
        #2: Center
rectangleType = 2


def nothing(x): 
    pass


camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
cv2.namedWindow('piCam')
cv2.createTrackbar('xVal','piCam',25,dispW,nothing) # trackbar automatically goes from 0 to some specified number, 25 is the initial value of trackbar and 500 is specified number
cv2.createTrackbar('yVal','piCam',25,dispH,nothing) # trackbar automatically goes from 0 to some specified number, 25 is the initial value of trackbar and 500 is specified number
cv2.createTrackbar('width','piCam',10,100,nothing)
cv2.createTrackbar('height','piCam',10,100,nothing)


#cam=cv2.VideoCapture(1)
while True:
     ret, frame=cam.read()
     xVal=cv2.getTrackbarPos('xVal','piCam')
     yVal=cv2.getTrackbarPos('yVal','piCam')
     width = cv2.getTrackbarPos('width','piCam')
     height = cv2.getTrackbarPos('height','piCam')
     cv2.circle(frame,(xVal,yVal),5,(255,0,0),-1)
     if rectangleType==1:
        cv2.rectangle(frame,(xVal,yVal),(int(width/100*(dispW-xVal)+xVal),int(height/100*(dispH-yVal)+yVal)),(255,255,255),2)
     if rectangleType==2:
         cv2.rectangle(frame,(int(xVal-width/100*dispW/2),int(yVal-height/100*dispH/2)),((int(xVal+width/100*dispW/2),int(yVal+height/100*dispH/2))),(255,255,255),2)
     cv2.imshow('piCam',frame)
     cv2.moveWindow('piCam',0,0)
     wait = cv2.waitKey(1)
     if wait==ord('q'):
         break
     
cam.release()
cv2.destroyAllWindows()



