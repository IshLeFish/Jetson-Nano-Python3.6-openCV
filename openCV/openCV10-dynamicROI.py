import cv2
print(cv2.__version__)


dispW=640
dispH=480
flip=2

x1=0
y1=0
x2=0
y2=0
state = 0
xinit=0
yinit=0
xfinal=0
yfinal=0

def click(event,x,y,flags,params):
    global x1
    global x2
    global y1
    global y2
    global state
    global xinit
    global yinit
    global xfinal
    global yfinal

    
    #print(xinit)
    if event==1:
        print(x)
        xinit=x
        yinit=y
        state=2
    if event==4:
        xfinal = x
        yfinal = y
        x1=xinit
        x2=xfinal
        y1=yinit
        y2=yfinal
        state=1

cv2.namedWindow('piCam')
cv2.setMouseCallback('piCam',click)

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(1)
while True:
     ret, frame=cam.read()
     #print(state,"|",x1,",",y1)
     cv2.rectangle(frame,(x1,y1),(x2,y2),(255,255,255),4)

     if state == 1:
        roi=frame[y1:y2,x1:x2]
        cv2.imshow('roi',roi)
        cv2.moveWindow('roi',dispW+50,0)

     cv2.imshow('piCam',frame)
     cv2.moveWindow('piCam',0,0)

     if cv2.waitKey(1)==ord('q'):
         break
cam.release()
cv2.destroyAllWindows()