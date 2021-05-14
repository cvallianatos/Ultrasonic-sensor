import RPi.GPIO as GPIO
import time

def pulseIn(echoPin):
   while GPIO.input(echoPin)==0:
      pulse_start = time.time()
   while GPIO.input(echoPin)==1:
      pulse_end = time.time() 
   
   pulse_duration = pulse_end - pulse_start
	
   return pulse_duration

def scan():
   TRIG = 23
   ECHO = 24

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
   return

def main():
   GPIO.setmode(GPIO.BCM)
   while True: 
      scan()
   GPIO.cleanup()

if __name__ == '__main__':
   main()
