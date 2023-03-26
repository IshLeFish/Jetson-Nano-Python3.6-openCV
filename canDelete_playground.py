import cv2
import time
print(cv2.__version__)

dispW = 640
dispH = 480

boxW = 10
boxH = 8
boxThickness = 2

boxX=0
boxY = 0

stageX = 1
stageY = 1

while True:

    print(boxY) 

    if boxX >= dispW-boxW and stageX == 1:
        stageX = 2
    if boxX <= 0 and stageX == 2:
        stageX = 1

    if boxY >= dispH-boxH and stageY == 1:
        stageY = 2
    if boxY <= 0 and stageY == 2:
        stageY = 1

    if stageX == 1:
        boxX+=1
    if stageX == 2:
        boxX-=1
    

    if stageY == 1:
        boxY+=1
    if stageY == 2:
        boxY-=1

    time.sleep(1/30)

print("Quit")
