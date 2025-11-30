#include <Wire.h>
#include <AS5600.h>
#include <PID_v1.h>
AS5600  as5600;  //create sensor object
unsigned long currentMs;  //current time variable
unsigned long lastMs;     // time of last measurement
const unsigned int FREE_RUN_PERIOD_MS = 100; //sampling period
float sig_angle_deg;  // angle measurement

// Motor control pins
const int motorPin1 = 10; // IN1 
const int motorPin2 = 11; // IN2 
const int enablePin = 9;  // ENA (PWM pin for speed control)

// Encoder pin
const int encoderPin = 2; // use just one encoder pin for simplicity
unsigned long lastOutputChange = 0;
volatile int pulseCount = 0;  // pulse counter
const int pulsesPerRevolution = 11; // pulses per rotation from each encoder wire

unsigned long lastTime = 0;   // store last time measurement
double frequency = 0;         // measured frequency

int graphinterval = 100; //in milliseconds

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

double reductionRatio = 4.4;

double wheelRPM = 0;

void countPulse();

void setup() {
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(enablePin, OUTPUT);

  pinMode(encoderPin, INPUT_PULLUP); // 1 encoder input

  attachInterrupt(digitalPinToInterrupt(encoderPin), countPulse, RISING);
  Wire.begin();     // Initialize I2C
  as5600.begin();   // Initialize sensor
  lastTime = millis();  // Initialize timing
  Serial.begin(9600);  // Initialize Serial Monitor

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

    // Motor direction + speed
  if (motorCmd > 0) 
  {
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
    
  } 
  else 
  {
    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, LOW);
    
   
  }

  analogWrite(enablePin, abs(motorCmd));
  
  // Frequency calculation every 0.5 seconds
  if (millis() - lastTime >= graphinterval) {
    noInterrupts();
    int count = pulseCount;
    pulseCount = 0;
    interrupts();

    frequency = count / (pulsesPerRevolution*(graphinterval/100)); // frequency in Hz
    wheelRPM = (count * 60.0) / (reductionRatio);
// waardes opslaan in lijst om te plotten
    Serial.print("Output: ");
    Serial.print(motorCmd);
    Serial.print("  Frequency: ");
    Serial.print(frequency);
    Serial.print(" Hz");
    Serial.print(" Wheel RPM: ");
    Serial.print(wheelRPM);


    lastMs = currentMs;
    // sig_angle_deg = (float)as5600.readAngle()*0.0879; //0.0879=360/4096;  // degrees [0..360)
    Serial.print(String(" Angle: ") + sig_angle_deg + '\t');
    Serial.println();  
    lastTime = millis();
  }
}

void countPulse() {
  pulseCount++;  // increment each pulse
}