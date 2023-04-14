import time
import RPi.GPIO as GPIO
from Buzzer import Buzzer

GPIO.setmode(GPIO.BCM)
buzzer = Buzzer(14) # Buzzer Objekt erstellen
time.sleep(0.5)
buzzer.on() # Ton starten

time.sleep(1)
buzzer.setFrequency(300) # Frequenz ändern auf 300Hz
time.sleep(1)

# Beenden
buzzer.stop()
GPIO.cleanup()