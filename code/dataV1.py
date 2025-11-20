import numpy as np
import matplotlib.pyplot as plt


RWM = np.array([])
RPM = np.array([441.41,418.75, 412.26,407.93,402.52, 398.19,392.78,396.03,388.45,380.88,374.33,362.48,349.50, 335.43, 315.96,299.73,277.00,252.12,219.63,181.78,136.34,0,0,0,0,0,0,0,0,0,0, 51.94,121.19,174.21,217.49,246.71,277.0,298.64,318.12,335.43,348.42,361.40,371.14,378.71,386.29, 392.78,397.11,402.52,407.93,413.34,417.67,440.39 ])
frequency = np.array([74.0, 70.18, 69.09, 68.36, 67.45, 66.73, 65.82,64.73, 63.64, 62.55, 60.91,   59.09,56.91, 54.55, 51.64, 48.36, 45.27,40.73,35.45,29.09, 0, 0, 0 ,0 , 0, 0 ,0,0 ,0 ,0 ,0, 8.73, 21.45, 30.18, 36.91, 42.55, 46.73,50.18, 53.64, 56.73, 58.91, 60.73, 62.36, 63.64, 64.91,66.0,67.09,67.82,68.55,69.45,70.36, 74.18])
x = 255

while x >=-255:
    RWM = np.append(RWM, x)
    x-=10

# plt.scatter(RWM, frequency)
# plt.xlabel("frequency (Hz)")
# plt.ylabel("RWM")
# plt.show()
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Output response grafieken')

ax1.scatter(frequency, RWM)
ax1.set_xlabel("frequency (Hz)")
ax1.set_ylabel("RWM")

ax2.scatter(RPM, RWM)
ax2.set_xlabel("RPM")
ax2.set_ylabel("RWM")

plt.tight_layout()
plt.show()