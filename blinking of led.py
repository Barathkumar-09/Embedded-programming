import RPi.GPIO as GPIO     
from time import sleep  
led_pin = 21 
GPIO.setup(led_pin, GPIO.OUT)  
pwm = GPIO.PWM(led_pin, 100)   
pwm.start(0)                                   
for x in range(100): 
  b=int(input("Enter the brigthness :"))
  pwm.ChangeDutyCycle(b)   
pwm.stop()
