import sys
import time
import RPi.GPIO as GPIO
from Buzzer import Buzzer

GPIO.setmode(GPIO.BCM)
buzzer = Buzzer(14)
time.sleep(0.5)
buzzer.on()

time.sleep(1)
buzzer.setFrequency(300)
time.sleep(1)
GPIO.cleanup()
sys.exit()