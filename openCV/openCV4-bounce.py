import cv2
print(cv2.__version__)


dispW=640
dispH=480
flip=0 # flip because raspi cam is upside down

boxW = 120
boxH = 100
boxThickness = 10

boxX=0
boxY = 0

stageX = 1
stageY = 1

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(1)
while True:
    ret, frame=cam.read()
     
     
    if boxX >= dispW-boxW and stageX == 1:
        stageX = 2
    if boxX <= 0 and stageX == 2:
        stageX = 1

    if boxY >= dispH-boxH and stageY == 1:
        stageY = 2
    if boxY <= 0 and stageY == 2:
        stageY = 1

    if stageX == 1:
        boxX+=5
    if stageX == 2:
        boxX-=5
    

    if stageY == 1:
        boxY+=5
    if stageY == 2:
        boxY-=5

    frame=cv2.rectangle(frame,(boxX,boxY),(boxX+boxW,boxY+boxH),(255,255,255),boxThickness) #add a rectangle to the frame using openCV(CV2), identify topleft and bottomright coords, choose colour (BGR), linewidth
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
