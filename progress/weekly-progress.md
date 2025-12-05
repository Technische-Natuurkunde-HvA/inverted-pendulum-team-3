
# Week 4 

## 1. Progress description

- We tested the PID code from week 2, it worked fine after some minor tweaks.(see map inverted-pendulum-team-3\code\Arduino\PIDController)
- With the pendulum starting in the middle position, it could correct for being pushed to the left and the right.
- In the middle position, the flywheel still spins but slows down to a halt after enough time.
- It can't yet lift itself up from a bumber position. In that case the flywheel will keep spinning faster and faster in one direction and the systems starts shaking voilently. 
- We think we can fix this with some additional code

## 2. Code (main focus this week)
```c
// PID tuning parameters
double Kp = 30.0;
double Ki = 0.0;
double Kd = 0.5;
```
- this simple configuration worked the best. Adding a small postive Kd made the flywheel slowly stop spinning, but too big and it seemed to have a negative impact on the stability.
## 3. Results

## 4. Reflection

# Week 3

## 1. Progress description

- We made a pyserial connection so we can pass the data from the arduino to python. We made a file that will update the graph real time and put it into a csv.
- We made a csvreader so we can easily read out the csv's and reproduce the graphs. 
- We set up the angle sensor in our setup and did some testing.
- We made a new wheel because the old one was too small and wouldnt lift. We have lifted the wheel multiple times during testing and made it so it slows down the more to the center it gets.
- We tested our PID controller and compared it to the one that we got access to this week (https://github.com/br3ttb/Arduino-PID-Library). We found out that its nearly identical since we already use the same library. 
- We updated our RPM formula since we used a wrong formula. We updated the outputresponse graph with the right RPM.
- We came up with a way to not lose any progress while commiting/pushing with multiple people at the same time.
- Our arduino had some issues, we had a work around but in the end got a new one
- We thought of a way to deal with the deadzone of our motor

## 2. Code
```c 
double Setpoint = 0;     // target angle
double Input    = 0;     // current angle
double output   = 0;     // PID output (-255..255)
double deadzone = 45;    // zone of the motor where it doesnt spin

// PID tuning parameters
double Kp = 2.0;
double Ki = 5.0;
double Kd = 0.5;

// Create PID controller
PID anglePID(&Input, &output, &Setpoint, Kp, Ki, Kd, DIRECT);
void setup() {
// theres more code but not relevant to the code progress


// PID config
  anglePID.SetMode(AUTOMATIC);
  anglePID.SetOutputLimits(-210, 210);  // motor control range
  

  // -------- Set your desired angle here --------
  Setpoint = 240;  // target angle (0–360 degrees)
}
void loop() {
  double angleDeg = as5600.readAngle() * 0.0879;

  Input = angleDeg;
    
  

  // Run PID
  anglePID.Compute();


  double motorCmd = output;
  
  // adds or substracts the deadzone based on if its positive or negative
  motorCmd = 
    (motorCmd>0) ? (motorCmd+ deadzone):
    (motorCmd<0) ? (motorCmd-deadzone):
        0;


    
    motorCmd = constrain(motorCmd, -255, 255); //makes sure the output stays in the range of the motor

  analogWrite(enablePin, abs(motorCmd));}
  ``` 
 ```python

    #generates the current date and time
  filename = f"data_{now.strftime('%d-%m-%Y_%H-%M')}.csv"

  pattern = re.compile(
    r"Output:\s*([-0-9.]+)\s*Frequency:\s*([-0-9.]+)\s*Hz\s*Wheel RPM:\s*([-0-9.]+)\s*Angle:\s*([-0-9.]+)")

#declaration of lists and variables
anglelist = []
rpmlist = []
outputlist= []
timelist = []
currenttime = 0 

# activates interactive pyplot
plt.ion()

#defining what the graphs look like (whats in it etc)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))
anglegraph, = ax1.plot([], [], label="Angle")
outputgraph, = ax2.plot([],[], label="Output")
rpmgraph, = ax3.plot([],[], label="RPM")

# setting x label
ax1.set_title("Time (s)")
ax2.set_title("Time (s)")
ax3.set_title("Time (s)")

# setting y label
ax1.set_ylabel("Angle (degrees)")
ax2.set_ylabel("Output")
ax3.set_ylabel("RPM")

#activating the legend
ax1.legend()
ax2.legend()
ax3.legend()

try:
    while time.time() - start < duration:
        line = ser.readline().decode().strip()
        print(line)
        match = pattern.search(line)
        if match:
            # uses the split output from the arduino and makes it variabel (float)
            output = float(match.group(1))
            freq   = float(match.group(2))
            rpm    = float(match.group(3))
            angle  = float(match.group(4))

            # adds the variables to the list
            timelist.append(time.time() - start)
            anglelist.append(angle)
            rpmlist.append(rpm)
            outputlist.append(output)

            # Sets the data for the live graphs            
            anglegraph.set_xdata(list(timelist))
            anglegraph.set_ydata(list(anglelist))

            outputgraph.set_xdata(list(timelist))
            outputgraph.set_ydata(list(outputlist))

            rpmgraph.set_xdata(list(timelist))
            rpmgraph.set_ydata(list(rpmlist))

            #autoscale
            ax1.relim();  ax1.autoscale_view()
            ax2.relim();  ax2.autoscale_view()
            ax3.relim();  ax3.autoscale_view()

            plt.pause(0.01)

except KeyboardInterrupt:
    print("Stopped.")
    
finally:
    ser.close()        

# sets it to a data set so it can be exported as csv
data = {
    "Time": timelist,
    "Angle": anglelist,
    "Output": outputlist,
    "RPM": rpmlist
}

df = pd.DataFrame(data)
df.to_csv(f'data/{filename}', index=False)
```


## 3. Results
- ![as mentioned above we updated our OutputResponse curve. We replaced the old one with the new one (OutputResponseCurve.png)](OutputResponseCurve.png)
- Angle sensor works
- Every variable we can measure gets send to python during measurements. We can now observe what happens during measurements with live data. This can be especially useful when we start using our PID next week and need to adjust the PID values because we can monitor the effects on the RPM, ouput and angle. We havent added the pyserial code to the code section since we felt like we already have a lot of code. What happens in the python code is takes the string given by the arduino. It breaks it up and it parces it into a float so we can use it for the graphs. Once the connection/measurement has finished it gets turned into a csv. 
- We lifted the wheel and it slowed down when it came closer to the center. We did this by editing supplied code, our plan is to use this code later when we got our PID working to make the wheel be able to center itself from every position.
- We decided that Joran will manually merge things if needed since we lost a tiny bit of progress when someone else pushed something. Joran will put in the commits if someone else made/contributed to it. 
- Our arduino didnt wanna flash new code, we found a fix for it but it was not ideal. We had to manually reset the arduino everytime we wanted to flash code onto the arduino. Now we have a different arduino that works.
- We fixed the deadzone issue of our engine through decreasing the PID range by the deadzone and then adding/substracting the deadzone. So for example if the PID has a range of (-255,255) it can give an output of 40 this is in our deadzone so the wheel would do nothing. What it does now is it give an output in the range of (-210,210) and we add or substract the deadzone. So an output of 40 would be 40+45 = 85. This is not in the deadzone and so it will spin. We have not tested it yet but we have ran it by Mark.

## 4. Reflection
- We learned that our wheel was too small and the physics behind it. The moment of inertia is defined as mass times radius^2. We had a small radius and a heavy wheel so it wasnt lifting up. We increased r and now it works. 
- We learned that we should be careful with changing the output too fast since it can damage the motor. 

- We are gonna focus on finding the most ideal PID values. We are gonna do this by trial and error and following the things we learnt with math class. Once we have the ideal PID values we are gonna add the code supplied during class so the wheel can start on the side.
- We are gonna focus on optimizing the code and try to make it faster and more effecient.

# Week 2

## 1. Progress description
- We changed the code so it accelarates and deccelarates a set amount from -255 to 255 PWM. 
- We added an RPM output. 
- We hought about how the entire system would come together in the end and made a simple flowchart out of it. 
- We researched the language of code needed for arduino so we can understand it better. 
- We have made an outputresponsecurve, we have done that through python where we read the data in the arduino IDE and hardcoded it in python for a first version (python code: "dataV1.py"). 

## 2. Code

```c
if (millis() - lastOutputChange >= 1000 && negativeOutputChange == true) {  // every 1000 ms
    if(output == -255){
      negativeOutputChange = false;
      lastOutputChange = millis();
      
    }
    else{
      output -= 10;      // decrease speed
      lastOutputChange = millis();
    }
  }
  else if(millis() - lastOutputChange >= 1000 && negativeOutputChange == false){
      if(output == 255){
      negativeOutputChange = true;
      lastOutputChange = millis();
      
      }
    
    else{
      output += 10;      // decrease speed
      lastOutputChange = millis();
    }```


``` 
## 3. Results



- Like mentioned above we made a flowchart (FlowChartV1.jpeg). It starts as it shows with the wheel, the wheel has a certain position and that position gets measured with the angle sensor. The angle sensor then gives the angle to a python file and the PID controller, the python file will have live data so we can have live graphs and data visualization. The PID controller will make an adjustment in the output based on the current angle and the desired angle. After the adjustment is made it goes back to the angle sensor and thats how we wanna setup our code.
- We also made a video to demonstrate the change of output (V1.mp4)
- We also made an outputresponsegraph both with the frequency and rpm. we set everything between -55 and 55 to 0 because the engine doesnt have enough power to spin it but it still had momentum. 


## 4. Measurement protocol
We will measure the PWM values from 50 to 255 and -50 to -255. We choose for this because we observed that the wheel isnt spinning from -50 to 50. We want to perform 3 measurements per value and steps of 10 so it doesnt take too long and we still get enough data points. We are gonna measure both sides so the negative and the positive to see if theres a noticable difference. We want to setup a pyserial connection to python to visualize the data there. 

## 5. Reflection 


- We learned to code the arduino and learned how the pid would be used we havent added yet but we have seen a use for it. 
- We should improve that the wheel actually gets lifted by the torque, and to automate the data because for the first time we think its okay to hard code the data from the arduino IDE to python but we do need to automate it. 
- We are gonna establish a pyserial connection in the coming week. 
- We are going to attached and integrate the anglular sensor. 



