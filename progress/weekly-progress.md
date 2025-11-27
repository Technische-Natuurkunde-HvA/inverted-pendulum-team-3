

# Week 1

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


We learned to code the arduino and learned how the pid would be used we havent added yet but we have seen a use for it. We should improve that the wheel actually gets lifted by the torque, and to automate the data because for the first time we think its okay to hard code the data from the arduino IDE to python but we do need to automate it. We are gonna establish a pyserial connection in the coming week. We also are going to attached and integrate the anglular sensor. 


# Week 2

## 1. Progress description

- We made a pyserial connection so we can pass the data from the arduino to python. We made a file that will update the graph real time and put it into a csv. 
- We set up the angle sensor in our setup and did some testing.
- We made a new wheel because the old one was too small and wouldnt lift. We have lifted the wheel multiple times during testing and made it so it slows down the more to the center it gets.
- We tested our PID controller and compared it to the one that we got access to this week (https://github.com/br3ttb/Arduino-PID-Library). We found out that its nearly identical since we already use the same library. 
- We updated our RPM formula since we used a wrong formula. We updated the outputresponse graph with the right RPM.
- We came up with a way to not lose any progress while commiting/pushing with multiple people at the same time.
- Our arduino had some issues, we had a work around but in the end got a new one

## 2. Code




## 3. Results
- As mentioned above we updated our OutputResponse curve. We replaced the old one with the new one (OutputResponseCurve.png)
- Angle sensor works
- Every variable we can measure gets send to python during measurements. We can now observer what happens during measurements with live data. This can be especially useful when we start using our PID next week and need to adjust the PID values because we can monitor the effects on the RPM, ouput and angle. 
- We lifted the wheel and it slowed down when it came closer to the center. We did this by editing supplied code our plan is to use this code later when we got our PID working to make the wheel be able to center itself from every position.
- We decided that Joran will manually merge things if needed since we lost a tiny bit of progress when someone else pushed something. Joran will put in the commits if someone else made a made/contributed to it. 
- Our arduino didnt wanna flash new code, we found a fix for it but it was not ideal. We had to manually reset the arduino everytime we wanted to flash code onto the arduino. Now we have a different arduino that works.

## 4. Reflection
- We learned that our wheel was too small and the physics behind it. The moment of inertia is defined as mass times radius^2. We had a small radius and a heavy wheel so it wasnt lifting up. We increased r and now it works. 
- We learned that we should be careful with changing the output too fast since it can damage the motor. 

- We are gonna focus on finding the most ideal PID values. We are gonna do this by trial and error and following the things we learnt with math class. Once we have the ideal PID values we are gonna add the code supplied during class so the wheel can start on the side. 
