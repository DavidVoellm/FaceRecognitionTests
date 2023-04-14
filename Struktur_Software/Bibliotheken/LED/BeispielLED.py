import led
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED = led.LED() # LED Objekt erstellem
LED.test() # test Funktion durchlaufen lassen

#beenden
GPIO.cleanup()