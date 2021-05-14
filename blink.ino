int red_led = 8;
int yellow_led = 9;
int green_led = 10;
int blue_led = 19;
int white_led = 18;

void setup() {
   pinMode(red_led, OUTPUT);
   pinMode(yellow_led, OUTPUT);
   pinMode(green_led, OUTPUT);
   pinMode(blue_led, OUTPUT);
   pinMode(white_led, OUTPUT);
}

void loop() {
   digitalWrite(red_led, HIGH);
   delay(100);
   digitalWrite(red_led, LOW);
   delay(100);

   digitalWrite(yellow_led, HIGH);
   delay(100);
   digitalWrite(yellow_led, LOW);
   delay(100);

   digitalWrite(green_led, HIGH);
   delay(100);
   digitalWrite(green_led, LOW);
   delay(100);
 
   digitalWrite(blue_led, HIGH);
   delay(100);
   digitalWrite(blue_led, LOW);
   delay(100);

   digitalWrite(white_led, HIGH);
   delay(100);
   digitalWrite(white_led, LOW);
   delay(100);
}

