import cv2
print(cv2.__version__)

def nothing():
    pass

cv2.namedWindow('blended')
cv2.createTrackbar('blendValue','blended',50,100,nothing)

dispW=320
dispH=int(dispW/640*480)
flip=2


cvLogo = cv2.imread('cv.jpg')
cvLogo=cv2.resize(cvLogo,(dispW,dispH))
cvLogoGray=cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY)
cv2.imshow('cv Logo Gray', cvLogoGray)
cv2.moveWindow('cv Logo Gray', 0,int(dispH*5/3))

_,BGMask=cv2.threshold(cvLogoGray,170,255,cv2.THRESH_BINARY)
cv2.imshow('BG Mask', BGMask)
cv2.moveWindow('BG Mask', dispW+55,int(dispH/3))

FGMask=cv2.bitwise_not(BGMask)
cv2.imshow('FGMask',FGMask)
cv2.moveWindow('FGMask',dispW+55,int(dispH*5/3))

FG=cv2.bitwise_and(cvLogo,cvLogo,mask=FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG',dispW*2+55,int(dispH*5/3))



camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(1)
while True:
     ret, frame=cam.read()
     cv2.imshow('piCam',frame)
     cv2.moveWindow('piCam',0,int(dispH/3))

     BG = cv2.bitwise_and(frame,frame,mask=BGMask)
     cv2.imshow('BG',BG)
     cv2.moveWindow('BG',dispW*2+55,int(dispH*1/3))

     compImage=cv2.add(FG,BG)
     cv2.imshow('compImage',compImage)
     cv2.moveWindow('compImage',dispW*3+55,int(dispH*1/3))

     BV=cv2.getTrackbarPos('blendValue','blended')/100


     Blended=cv2.addWeighted(frame,BV,cvLogo,1-BV,0) # make a blended foreground, 50% frame, 50% logo, random other variable keep 0
     cv2.imshow('blended',Blended)
     cv2.moveWindow('blended',dispW*3+55,int(dispH*5/3))
     
     FG2=cv2.bitwise_and(Blended,Blended,mask=FGMask)
     cv2.imshow('FG2',FG2)
     cv2.moveWindow('FG2',dispW*4+55,int(dispH*1/3))

     compFinal=cv2.add(FG2,BG)
     cv2.imshow('compFinal',compFinal)
     cv2.moveWindow('compFinal',dispW*4+55,int(dispH*5/3))





     if cv2.waitKey(1)==ord('q'):
         break
cam.release()
cv2.destroyAllWindows()