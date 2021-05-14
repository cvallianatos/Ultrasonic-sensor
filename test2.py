import os
import glob
from gpiozero import LED
from time import sleep

def main():
   led_red = LED(14)
   led_yellow = LED(15)
   led_green = LED(18)

   myFlag = True
   while myFlag: 
      print("Main Menu")
      print("---------")
      print("(R) RED")
      print("(Y) YELLOW")
      print("(G) GREEN")
      print("(S) Scan Sensor")
      print("(E) Exit") 

      myOption = input()
      myOption = myOption.upper()
      
      if myOption == "E":
         myFlag = False
      elif myOption == "R":
         led_red.on()
         sleep(1)
         led_red.off()
         sleep(1)
      elif myOption == "Y":
         led_yellow.on()
         sleep(1)
         led_yellow.off()
         sleep(1)
      elif myOption == "G":
         led_green.on()
         sleep(1)
         led_green.off()
         sleep(1)
      elif myOption == "S":
         sleep(1)
      else:
         print("Please select a valid option.")
         print("Press enter to continue.")
         myOption = input()
   return

if __name__ == '__main__':
   main()
