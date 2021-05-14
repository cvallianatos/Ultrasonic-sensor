// ---------------------------------------------------------------- //
// Ultrasoninc Sensor HC-SR04
// Using Arduino IDE 1.8.7
// Using HC-SR04 Module
// by Chris Vallianatos
// April 20, 2021
// ---------------------------------------------------------------- //

#define echoPin 18 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 19 //attach pin D3 Arduino to pin Trig of HC-SR04

#define redPin 8
#define yellowPin 9
#define greenPin 10

// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  pinMode(redPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
}

void loop() {
 
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor and turns on or off the LEDs
  if (distance < 75)
  {
     digitalWrite(redPin, HIGH);
     digitalWrite(yellowPin, LOW);
     digitalWrite(greenPin, LOW);   
  }
  if (distance > 75 && distance < 100)
  {
     digitalWrite(redPin, LOW);
     digitalWrite(yellowPin, HIGH);
     digitalWrite(greenPin, LOW);   
  }
  if (distance > 100)
  {
     digitalWrite(redPin, LOW);
     digitalWrite(yellowPin, LOW);
     digitalWrite(greenPin, HIGH);   
  }
}
