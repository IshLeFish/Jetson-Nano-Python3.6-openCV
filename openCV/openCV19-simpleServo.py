import cv2
print(cv2.__version__)
from adafruit_servokit import ServoKit

myKit = ServoKit(channels=16)

import time
myKit.servo[0].angle = 80
myKit.servo[1].angle = 180
#for i in range(0,180,1):
#    myKit.servo[0].angle = i
#    myKit.servo[1].angle = 180-i
#    time.sleep(.01)
#for i in range(180,0,-1):
#    myKit.servo[0].angle = i
#    myKit.servo[1].angle = 180-i
#    time.sleep(.01)