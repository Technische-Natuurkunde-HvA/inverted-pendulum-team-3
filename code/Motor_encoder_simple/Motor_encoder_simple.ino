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

double output = 255;    // motor output value

bool negativeOutputChange = true ;     // variable to dictate which direction the output needs to change to

double d_wheel = 12.3;
double d_engine = 2.44;

double reductionRatio = d_wheel/d_engine;

double wheelRPM = 0;

void countPulse();

void setup() {
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(enablePin, OUTPUT);

  pinMode(encoderPin, INPUT_PULLUP); // 1 encoder input

  attachInterrupt(digitalPinToInterrupt(encoderPin), countPulse, RISING);

  Serial.begin(9600);
  lastTime = millis();
}

void loop() {
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
    }
    
  }
 
  // Motor direction + speed
  if (output > 0) 
  {
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
    
  } 
  else 
  {
    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, LOW);
    
   
  }
  analogWrite(enablePin, abs(output));
  
  // Frequency calculation every 0.5 seconds
  if (millis() - lastTime >= 500) {
    noInterrupts();
    int count = pulseCount;
    pulseCount = 0;
    interrupts();

    frequency = count / (pulsesPerRevolution*0.5); // frequency in Hz
    wheelRPM = (count * 60.0) / (pulsesPerRevolution  * reductionRatio);
// waardes opslaan in lijst om te plotten
    Serial.print("Output: ");
    Serial.print(output);
    Serial.print("  Frequency: ");
    Serial.print(frequency);
    Serial.print(" Hz");
    Serial.print(" Wheel RPM: ");
    Serial.println(wheelRPM);

    lastTime = millis();
  }
}

void countPulse() {
  pulseCount++;  // increment each pulse
}