class Buzzer:
    pass
import sys
import RPi.GPIO as GPIO
import time

triggerPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPIN,GPIO.OUT)

buzzer = GPIO.PWM(triggerPIN, 1000) # Set frequency to 1 Khz
buzzer.start(10) # Set dutycycle to 10

time.sleep(1)
GPIO.cleanup()
sys.exit()