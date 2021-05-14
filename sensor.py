import RPi.GPIO as GPIO
import time

def pulseIn(echoPin):
   while GPIO.input(echoPin)==0:
      pulse_start = time.time()
   while GPIO.input(echoPin)==1:
      pulse_end = time.time() 
   
   pulse_duration = pulse_end - pulse_start
	
   return pulse_duration

def ledAction(ledColor, action):
   # ledColor is pin associated with color
   # action True = ON, action False = OFF
   GPIO.setup(ledColor,GPIO.OUT)
   GPIO.output(ledColor, action)
   return

def ledTest(ledColor):
   GPIO.setup(ledColor,GPIO.OUT)
   GPIO.output(ledColor, True)
   time.sleep(2)
   GPIO.output(ledColor, False)
   return

def scan(TRIG, ECHO):
   GPIO.setup(TRIG,GPIO.OUT)
   GPIO.setup(ECHO,GPIO.IN)
   GPIO.output(TRIG, False)

   time.sleep(1)
   GPIO.output(TRIG, True)
   time.sleep(0.00001)
   GPIO.output(TRIG, False)
   distance = pulseIn(ECHO) * 17150
   distance = round(distance, 2)
   print("Distance:",distance,"cm")
   return distance

def main():
   # Distance map
   red_zone = 50
   yellow_zone = 75

   # Pin setup
   trigger = 5
   echo = 6
   red = 13
   yellow = 19
   green = 26

   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)

   # Startup test flashing of the LEDs

   ledTest(red)
   ledTest(yellow)
   ledTest(green)

   # Duration in seconds

   duration = 60
   
   start = time.time()

   while (time.time() < start + duration): 
      distance = scan(trigger, echo)
      if distance < red_zone:
         ledAction(red, True)
         ledAction(yellow, False)
         ledAction(green, False)
      
      if distance > red_zone and distance < yellow_zone:
         ledAction(red, False)
         ledAction(yellow, True)
         ledAction(green, False)
      
      if distance > yellow_zone:
         ledAction(red, False)
         ledAction(yellow, False)
         ledAction(green, True)

   # Shutdown the LEDs

   ledAction(red, False)
   ledAction(yellow, False)
   ledAction(green, False)

   GPIO.cleanup()
   return

if __name__ == '__main__':
   main()
