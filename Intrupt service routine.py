# import modules
import RPi.GPIO as GPIO
import time
# setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

#ir
i=0
def ISRL2H():
    print("\nIntrupt service routine : Low to High Detected !\n")
    GPIO.output(8,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(8,GPIO.LOW)
    time.sleep(2)
    
def ISRH2L():
    print("\nIntrupt service routine : High to Low  Detected !\n")
    GPIO.output(3,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(3,GPIO.LOW)
    time.sleep(2)  

while True:
  p=input("Press High or Low for pin 32 and enter 1") 
  if(GPIO.input(12)==GPIO.LOW):
    print("Calling Intrupt Service Routine !!!")
    ISRH2L()
  else:
    print("Calling Intrupt Service Routine !!!")
    ISRL2H()    
