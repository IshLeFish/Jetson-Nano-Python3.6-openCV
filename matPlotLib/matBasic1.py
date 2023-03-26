#Yeah so i broke this, rewrite it without the inputs and you'll be good i reckon.

import matplotlib.pyplot as plt
import numpy as np
noOfCurves=int(input("How many lines on your graph?: "))
xMin=int(input("Minimum X value: "))
xMax=int(input("Mmaximum X value: "))
xDataPoints = int(input("How many datapoints? "))
x = np.linspace(xMin,xMax,xDataPoints)
xRange = np.linspace(0,0,xDataPoints)
print("In curve " , i , ", what do you want the power to be?")
power = float(input("x^[]: "))
y=x^power
plt.plot(x,y)

plt.grid(True)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Le Graph')
plt.plot(xRange-xMin,y,'-r')
plt.plot(xRange+xMax,y,'-r')
plt.show()