import cv2
import numpy as np
print(cv2.__version__)



evt=-1
coord=[]
label=[]

pnt=(0,0)
clr=(0,0,0)

img=np.zeros((250,250,3),np.uint8) #ask numpy to make a matrix of ZEROS, 250 high and 250 wide, with 3 values in each .. uint8=the variable type

def click(event,x,y,flags,params):
    global pnt
    global evt
    global clr
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event Was: ',event)
        pnt=(x,y)
        coord.append(pnt)
        
        evt=event
    if event==cv2.EVENT_RBUTTONDOWN:
        print('Mouse Event Was: ',event)
        print(x,y)
        evt=event
        pnt=(x,y)
        blue=frame[y,x,0] #row first, then column second | row=how far up/down, therefore y | column = how far left/right, therefore x | bgr value identification: blue=0,green=1,red=2 
        green=frame[y,x,1]
        red=frame[y,x,2]
        print('b:',blue,' | g:',green,' | g:',red)
        colourString='b:'+str(blue)+', g:'+str(green)+', r:'+str(red)
        img[:]=[blue,green,red]
        fnt=cv2.FONT_HERSHEY_PLAIN
        b = 255-int(blue)
        g = 255-int(green)
        r = 255-int(red)
        clr = (b,g,r)
        cv2.putText(img,colourString,(10,25),fnt,1,clr,2)

        cv2.imshow('myColour',img)



dispW=640
dispH=480
flip=2
cv2.namedWindow('piCam')
cv2.setMouseCallback('piCam',click)

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(1)
while True:
     ret, frame=cam.read()
     font=cv2.FONT_HERSHEY_PLAIN
     
     for pnts in coord:
         cv2.circle(frame,pnts,5,(0,0,255),-1)
         myStr = str(pnts)
         cv2.putText(frame,myStr,pnts,font,1.5,(255,255,0),1)
     if evt==2:
         cv2.circle(frame,pnt,5,clr,2)
     cv2.imshow('piCam',frame)
     cv2.moveWindow('piCam',0,0)
     keyEvent = cv2.waitKey(1)
     if keyEvent==ord('q'):
         break
     if keyEvent==ord('c'):
        coord=[]
        evt=-1
        #pnt = pnt * 0
cam.release()
cv2.destroyAllWindows()