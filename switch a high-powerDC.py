Import RPi.GPIO as GPIO
Import time
in1 = 16
in2 = 18
GPIO.setmode (GPIO.BOARD)
GPIO.setup (in1, GPIO.OUT)
GPIO.setup (in2, GPIO.OUT)
GPIO.output (in1, False)
GPIO.output (in2, False)
While True:
      For x in range (5):
            GPIO.output (in1, True)
            Time. Sleep (0.1)
            GPIO.output (in1, False)
            GPIO.output (in2, True)
            Time. Sleep (0.1)
            GPIO.output (in2, False)
