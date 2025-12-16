# Brief project description – Team 3
Students from Applied Physics at the HvA in the Netherlands have build and stabilized a rotating inverted wheel pendulum. The team has stabilized the system by using an electric driven motor controlled by an Arduino microcontroller. The code for the system was partly given and some adjustments have been added to complete the goals the team set for themselves. 
---
## Folder explanations
```text
---inverted-pendulum-team-3     
    |   README.md
    |   
    +---code
    |   |   README.md
    |   |   
    |   +---Arduino
    |   |   +---AS5600_simple        
    |   |   |       AS5600_simple.ino
    |   |   |       
    |   |   +---Motor_encoder_simple
    |   |   |       Motor_encoder_simple.ino
    |   |   |
    |   |   +---PIDController
    |   |   |       PIDController.ino
    |   |   |
    |   |   +---Swing_pendulum_simple
    |   |   |       Swing_pendulum_simple.ino
    |   |   |
    |   |   \---UpsideDownPendulum
    |   |           UpsideDownPendulum.ino
    |   |
    |   \---Python
    |           csvreader.py
    |           dataOutputResponseCurve.py
    |           LiveData.py
    |
    +---data
    |       DataUpsideDown.csv
    |       DataUpsideDownFinal.csv
    |       DataUpsideDownMeting.csv
    |       data_12-12-2025_13-51.csv
    |       data_22-11-2025_19-59.csv
    |       data_24-11-2025_10-57.csv
    |       data_24-11-2025_11-02.csv
    |       data_24-11-2025_11-32.csv
    |       data_25-11-2025_12-56.csv
    |       data_25-11-2025_13-08.csv
    |       data_25-11-2025_13-09.csv
    |       README.md
    |
    +---docs
    |       index.md
    |
    +---feedback
    |       feedback-week-2.md
    |       feedback-week-3.md
    |       feedback-week-4.md
    |
    +---progress
    |       weekly-progress.md
    |
    \---visuals
        |   README.md
        |
        +---figures
        |   |   FlowChartV1.jpeg
        |   |   FlowChartV1Digital.png
        |   |   OutputResponseCurve.png
        |   |   README.md
        |   |   setup.jpg
        |   |   UpsideDownGraph.png
        |   |   UpsideDownGraphFinal.png
        |   |
        |   \---Flowchart_upside_down
        |           FlowChartDigital.png
        |           Flowchart_upside_down.jpeg
        |           Support_for_flowchart.jpeg
        |
        \---videos
                liveData.mp4
                README.md
                UpsideDown.mp4
                UpsideDownDemonstratie.mp4
                V1.mp4
```
## 1. Project Motivation
Inverted pendulums are widely used in society and play an important role in our daily lives. They are systems that balance unstable structures using control theory to maintain stability. You can find them in robots, self-balancing vehicles, and even in some engineering applications such as building stabilization systems. Pendulums are an interesting system because they actively stabilize an unnatural and unstable position in real time using feedback and control.


---
## 2. System overview of the mechanical and electrical setup 
The mechanical setup is designed by a partner institution from Portugal. They've designed a 3D printed pendulum holder wich fits the electrical part of our setup perfectly. The flywheel has been through a couple of different versions to filter out some faults in the design. The final product has been designed by the team with the use of Tinkercad and Autodesk Fusion 360 and has completed all the milestones that needed to be reached. The electrical setup contains an JGA25-370 12V DC motor with an encoder of 24V. We've used AS5600 angle sensor wich measures the angle of our motor. The data from the sensor is send back into our code. 
![Our pendulum](visuals/figures/setup.jpg)

---
## 3. Control Principle
The basics
- We aim to keep our inverted flywheel pendulum upright, even though this position is naturally unstable.
- We use the motor attached to the flywheel to generate torque by accelerating or decelerating it.
- This torque should counteract gravity and push the pendulum back toward the vertical position

More technical details
- The system is controlled using a PID controller based on feedback from an angle sensor.
Our PID controller continuously processes the measured angle and angular velocity from our sensor to determine the appropriate motor command and resulting torque.
- The PID controller we used had 3 parameters; K_p, K_i and K_d, by tuning these parameters we made sure the motor generated the right amount of torque at the right time.
For this project we only had to focus on K_p, which focuses on the error in position and K_d which acts on the rate of change of that error. An integral term K_I​ was not required, as steady-state errors were negligible, so that parameter was left on zero.

To solve the upside-down challenge, that is, bringing the pendulum from the stable hanging-down position to the unstable upright position and balancing g it there, additional steps were added to the control logic. For this challenge, we first ensured that the pendulum was sufficiently close to the upright position before enabling the PID controller described above. If this condition was not yet satisfied, the motor was driven with a constant input whose sign was determined by the current direction of motion, thereby injecting energy into the system and increasing the swing amplitude until it was sufficient for the PID to take over.

A simple flowchart of how our setup works:

![FLowChart](visuals/figures/FlowChartV1Digital.png)
---

## 4. Implementation


### 4.1 Arduino Control Software 
- The main entry point is the motor_encoder_simple ([motor_encoder.ino](code/Arduino/Motor_encoder_simple/Motor_encoder_simple.ino)). With this file you can test the motor and with a bit of editing you can find the deadzone of the motor. The deadzone (the zone where the motor wants to spin but can´t because of friction and lack of power) is important later when you are using a PID controller. The reason for this is because the PID doesn´t automatically factor in the deadzone. So if you dont take that into account the PID won´t work on tiny adjustments because it just simply won´t spin. 
- We haven´t set the main control loop frequency since we took the PID code straight from the source (https://github.com/br3ttb/Arduino-PID-Library/blob/master/examples/PID_Basic/PID_Basic.ino), there´s no loop frequency there so we haven´t used it. However we have set a frequency of 10 Hz on the data because of the live data graphs we use. Now it looks fluent because it updates 10 times every second. 
- As mentioned above every 0.1 seconds the data gets updated. This includes the sensor readings, output, rpm and frequency. The updated data will be send to a python file to process the data live. However we also measure the angle at the start of every loop. This is needed for the PID controller cause the PID updates the motor output to make it spin and then we have set a limit for safety. We have used a constrain function (https://docs.arduino.cc/language-reference/en/functions/math/constrain/) to make sure the output values dont exceed the limit.


### 4.2 Python Tools

- When the pendulum is active we run [live_data.py](code/Python/LiveData.py). So we can monitor the output, RPM and angle. It asks how long the measurement will be and will run the time given to it. After the code is finished it will save the data in a csv towards [data](data). And it will also give the final graph. We´ve also created a csv reader ([csvreader.py](code/Python/csvreader.py)) that reproduces the final graph of any given file generated by [live_data.py](code/Python/LiveData.py). 
Heres an example: [liveData.mp4](visuals/videos/liveData.mp4)

- The OutputResponseCurve is generated by [dataOutputResponseCurve.py](code/Python/dataOutputResponseCurve.py). All the measured frequencies are coded into the file since we didn´t have a pyserial connection yet. 
![OutputResponseCurve](visuals/figures/OutputResponseCurve.png)
---
## 5. Experiments and Data
- We have tested the pyserial connection with the upside down challenge through just starting the python file and rotating the pendulum manually. The data is stored in this: [upside_down_data](data/DataUpsideDownFinal.csv) file. 
As you can see below the pyserial connection works. The graph shows a low RPM because the motor wasnt on. It was pure for testing. 

![Graph of angle, output and RPM](visuals/figures/UpsideDownGraph.png)

- Heres a video of the first time we managed to stabilize the pendulum upside down: [Demonstartion of the upside down challenge](visuals/videos/UpsideDown.mp4)

---
## 6. Results
- The pendulum stabilized and came to rest both during the upside down challange and the regular stabilizing challenge. The average time to stabilize the pendulum for the upside down challenge is around 20 seconds. The time for stabilizing the pendulum at an angle of 30 degrees is around the 5 seconds. The system is not that sensitive for distrubances, it balances itself fairly quickly when out of balance.
Some limitations with the design arose during the upside down challenge. The cords attatched to the motor got in the way while the pendulum turned through the     angle barrier, the barrier in wich the pendulum could stabilize itself again if it came to the top. So if the pendulum turned outside of those 30 degrees on one   side, the cords would get tangled and pulled on the motor and Arduino.
Heres the graph of our final measurement:
![UpsideDownGraphFinal](visuals/figures/UpsideDownGraphFinal.png)
as you can see it stabilized itself fairly quickly youy can see big jumps in the graph but thats because the angle measures from 0 to 359 in a circle so if the pendulum swings past 359 it goes back to 0. 

Heres a demonstration of our pendulum:
 [Demonstration Upside Down](visuals/videos/UpsideDownDemonstratie.mp4)

 
---
## 7. Project Timeline

### Week 1
- Start of the project.
- Started researching flywheel designs.
- Designed the first version of our flywheel.

### Week 2
- Started building the pendulum and printed the first version of our flywheel.
- We made our first flowchart [FlowChart](visuals/figures/FlowChartV1.jpeg).
- Made a first version of the OutputResponseCurve.
- Started testing the pendulum with different output values.
- Did research on how to implement a PID and how to use arduino code more effectively.

### Week 3
- We made the arduino connect to python for live data readings so every variable can be read live (output, RPM, angle, frequency)
- Integrated the angle sensor in our pendulum.
- We figured that our flywheel was too small and heavy for it´s size. So we designed a new flywheel and printed it out. When we tested the new flywheel, the pendulum lifted for the first time.
- Made a PID controller using the PID_V1 library and compared it to the one on GitHub (https://github.com/br3ttb/Arduino-PID-Library/blob/master/examples/PID_Basic/PID_Basic.ino). We saw that they were nearly identical. 
- Found an issue with working on the main branch we fixed it by manually merging the different versions of files.
- We implemented a solution for the deadzone. We lowered the PID range and added the deadzone after the PID gives the output to compensate.

### week 4
- Balanced the pendulum for the first time using a PID.
- Improved the PID parameters.
- We found out that the system shakes a lot. 

### week 5
- We choose to do the upside down challenge. We started by making a flowchart for the logic of the code. [Flowchart upside down](visuals/figures/Flowchart_upside_down).
- Implemented the logic into our code and tweaked it.
- We excecuted upside down challenge succesfully!
- We ran into an issue regarding the live data with the upside down code and solved the issue.
---
For more detailed information check:
- [Week 2-4 report](progress/weekly-progress.md)

---
## 8. Team and Credits
Team members:
- Joran Stavenuiter
- Onno Dijkman
- Fleur van Essen
- Rinus Appelman
- Floris de Weerd
- Luka Marcé
---
Team leader:
- Youssef El Bouhassa
--- 
Client:
- Hogeschool van Amsterdam
---






















