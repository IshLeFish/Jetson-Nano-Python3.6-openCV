import cv2
print(cv2.__version__)
import numpy as np

pnt = (0,0)
hue = 50
sat = 50
val = 50

img=np.zeros((250,250,3),np.uint8)

def nothing(x):
    pass

def click(event,x,y,flags,params):
    global pnt
    global hue
    global sat
    global val
    if event == cv2.EVENT_LBUTTONDOWN:
        pointBGR = frame[y-1:y+1,x-1:x+1]
        pointHSV = cv2.cvtColor(pointBGR,cv2.COLOR_BGR2HSV)
        
        pointHSV = pointHSV[0]
        pointHSV = pointHSV[0]
        hue,sat,val = pointHSV
        
        

        #img[:,0:125]=[l_b[0],l_b[1],l_b[2]]
        img[:
        ]=[frame[y,x,0],frame[y,x,1],frame[y,x,2]]
        cv2.imshow('myColour',img)
        
        
        

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)

cv2.createTrackbar('hueRange', 'Trackbars',15,179,nothing)

cv2.createTrackbar('satRange', 'Trackbars',15,255,nothing)

cv2.createTrackbar('valRange', 'Trackbars',15,255,nothing)


dispW=640
dispH=480
flip=0
cv2.namedWindow('piCam')
cv2.setMouseCallback('piCam',click)
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    #frame=cv2.imread('smarties.png')
    

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #hue = 130
    #sat = 110 
    #val = 89

    hueLow=hue-cv2.getTrackbarPos('hueRange', 'Trackbars')
    hueHigh=hue+cv2.getTrackbarPos('hueRange', 'Trackbars')

    satLow=sat-cv2.getTrackbarPos('satRange', 'Trackbars')
    satHigh=sat+cv2.getTrackbarPos('satRange', 'Trackbars')

    valLow=val-cv2.getTrackbarPos('valRange', 'Trackbars')
    valHigh=val+cv2.getTrackbarPos('valRange', 'Trackbars')

    l_b=np.array([hueLow,satLow,valLow]) #lower Bounds
    u_b=np.array([hueHigh,satHigh,valHigh]) #upper Bounds

    FGmask=cv2.inRange(hsv,l_b,u_b)
    #print(l_b, ",",u_b)
    cv2.imshow('FGmask',FGmask)
    cv2.moveWindow('FGmask',0,530)

    contours,_=cv2.findContours(FGmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=lambda x:cv2.contourArea(x), reverse=True) #sort the 'contours'. lambda (x) is a defined inline function, sort x by reverse contour area
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        if area>=50:
            (x,y,w,h)=cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

            #cv2.drawContours(frame,[cnt],0,(255,0,0),3)
    #cv2.drawContours(frame,contours,0,(255,0,0),3)
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()