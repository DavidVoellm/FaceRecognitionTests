from Servo import Servo
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

s = Servo(17) # Servo Objekt erstellen
s.setAngle(90) # Winkel setzen
time.sleep(2) # warten
s.setAngle(180)
time.sleep(2)
s.setAngle(0)
