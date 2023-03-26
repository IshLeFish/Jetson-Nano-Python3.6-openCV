import cv2
print(cv2.__version__)


dispW=640
dispH=480
flip=0

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(1)
while True:
     ret, frame=cam.read()
     roi=frame[50:250,200:400].copy() #row 50-250, column 200-400 | y THEN x
     roiGrey=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
     roiGrey=cv2.cvtColor(roiGrey,cv2.COLOR_GRAY2BGR)
     frame[50:250,200:400]=roiGrey
     cv2.imshow('ROI',roi)
     cv2.imshow('piCam',frame)
     cv2.imshow('GRAY',roiGrey)
     cv2.moveWindow('piCam',0,0)
     cv2.moveWindow('ROI',int(dispW*1.1),0)
     cv2.moveWindow('GRAY',int(dispW*1.1),250)
     if cv2.waitKey(1)==ord('q'):
         break
cam.release()
cv2.destroyAllWindows()