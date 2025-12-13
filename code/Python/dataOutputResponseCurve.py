import numpy as np
import matplotlib.pyplot as plt
import serial
import time

RWM = np.array([])
#measured frequencies
frequency = np.array([74.0, 70.18, 69.09, 68.36, 67.45, 66.73, 65.82,64.73, 63.64, 62.55, 60.91,   59.09,56.91, 54.55, 51.64, 48.36, 45.27,40.73,35.45,29.09, 0, 0, 0 ,0 , 0, 0 ,0,0 ,0 ,0 ,0, 8.73, 21.45, 30.18, 36.91, 42.55, 46.73,50.18, 53.64, 56.73, 58.91, 60.73, 62.36, 63.64, 64.91,66.0,67.09,67.82,68.55,69.45,70.36, 74.18])
#calculates the RPM 
RPM = 60*frequency/4.4
x = 255

while x >=-255:
    RWM = np.append(RWM, x)
    x-=10


plt.scatter(RWM, RPM)
plt.xlabel("RWM")
plt.ylabel("RPM")
plt.grid()
plt.tight_layout()
plt.show()



