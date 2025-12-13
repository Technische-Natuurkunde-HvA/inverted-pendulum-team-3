import serial
import time
import re
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# --- UPDATE THIS PORT ---
PORT = "COM5"       # Windows example
# PORT = "/dev/ttyACM0"   # Linux
# PORT = "/dev/tty.usbmodem1101"  # Mac

BAUD = 9600
duration = int(input("How long should the measurement be?:")) # choose a duration to measure e.g 20 (seconds)
# Open serial connection
ser = serial.Serial(PORT, BAUD, timeout=1)

start = time.time() # start time
now = datetime.now()
filename = f"data_{now.strftime('%d-%m-%Y_%H-%M')}.csv"



# makes sure the output can be split so we can use the values
pattern = re.compile(
    r"Output:\s*([-0-9.]+)\s*Frequency:\s*([-0-9.]+)\s*Hz\s*Wheel RPM:\s*([-0-9.]+)\s*Angle:\s*([-0-9.]+)")

#declaration of lists and variables
anglelist = []
rpmlist = []
outputlist= []
timelist = []
currenttime = 0 

plt.ion()

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))
anglegraph, = ax1.plot([], [], label="Angle")
outputgraph, = ax2.plot([],[], label="Output")
rpmgraph, = ax3.plot([],[], label="RPM")

ax1.set_title("Time (s)")
ax2.set_title("Time (s)")
ax3.set_title("Time (s)")

ax1.set_ylabel("Angle (degrees)")
ax2.set_ylabel("Output")
ax3.set_ylabel("RPM")


ax1.legend()
ax2.legend()
ax3.legend()

try:
    while time.time() - start < duration:
        line = ser.readline().decode().strip()
        print(line)
        match = pattern.search(line)
        if match:
            output = float(match.group(1))
            freq   = float(match.group(2))
            rpm    = float(match.group(3))
            angle  = float(match.group(4))

            timelist.append(time.time() - start)
            anglelist.append(angle)
            rpmlist.append(rpm)
            outputlist.append(output)
            
            anglegraph.set_xdata(list(timelist))
            anglegraph.set_ydata(list(anglelist))

            outputgraph.set_xdata(list(timelist))
            outputgraph.set_ydata(list(outputlist))

            rpmgraph.set_xdata(list(timelist))
            rpmgraph.set_ydata(list(rpmlist))

            ax1.relim();  ax1.autoscale_view()
            ax2.relim();  ax2.autoscale_view()
            ax3.relim();  ax3.autoscale_view()

            plt.pause(0.01)

except KeyboardInterrupt:
    print("Stopped.")
    
finally:
    ser.close()        


data = {
    "Time": timelist,
    "Angle": anglelist,
    "Output": outputlist,
    "RPM": rpmlist
}

df = pd.DataFrame(data)
df.to_csv(f'data/{filename}', index=False)


plt.ioff()
plt.close('all')


fig2, (ax1f, ax2f, ax3f) = plt.subplots(3, 1, figsize=(8, 10))

ax1f.plot(timelist, anglelist, label="Angle")
ax2f.plot(timelist, outputlist, label="Output")
ax3f.plot(timelist, rpmlist, label="RPM")

ax1f.set_ylabel("Angle (deg)"); ax2f.set_ylabel("Output"); ax3f.set_ylabel("RPM")
ax1f.set_xlabel("Time (s)");ax2f.set_xlabel("Time (s)");ax3f.set_xlabel("Time (s)")
ax1f.legend(); ax2f.legend(); ax3f.legend()

plt.tight_layout()
plt.show()

