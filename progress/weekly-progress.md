# About this document

This is a team document where you record your weekly progress. It is written in Markdown, which allows you to format content in a simple and readable way. The document is rendered directly in GitHub without the need for a compiler (unlike LaTeX). The syntax is relatively easy. An overview of commonly used Markdown syntax can be found here:  
https://www.markdownguide.org/basic-syntax/

Below you find an example of the sections that must be included in each weekly progress report.

Use the **same document for all weeks**. For each week, use the **same headers and subheaders**.

Use the GitHub repository to store important project files (code, visuals including videos and figures, data, etc.). If necessary refer to those files in this document using a hyperlink. 

---

# Week 1

## 1. Progress description
We changed the code so it accelarates and deccelarates a set amount from -255 to 255. We also added an RPM output. We also thought about how the entire system would come together in the end and made a simple flowchart out of it. We also researched the language of code needed for arduino so we can understand it better. 

## 2. Code

You can display code using three backticks (```) followed by an optional language extension.  
For example:  
- For C/C++ code, use `c` or `cpp`.  
- For Python, use `python`.
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

#### Example:

```c
// Header file for input/output functions
#include <stdio.h>

// Main function: entry point for execution
int main() {

    // Print a message to the console
    printf("Hello World");

    return 0;
}
``` 
## 3. Results
Present your results here. This may include tables, figures, or charts.
Add charts and other visuals to the `visuals` folder in the GitHub repository and reference them in this document if needed.


Like mentioned above we made a flowchart (FlowChartV1.jpeg).
We also made a video to demonstrate the change of output (V1.mp4)


## 4. Measurement protocol
We will measure the PWM values from 50 to 255 and -50 to -255. We choose for this because we observed that the wheel isnt spinning from -50 to 50. We want to perform 3 measurements per value and steps of 10 so it doesnt take too long and we still get enough data points. We are gonna measure both sides so the negative and the positive to see if theres a noticable difference. We want to setup a pyserial connection to python to visualize the data there. 

## 5. Reflection 
What did you learn this week?
What should you focus on or improve in the coming weeks of the project?