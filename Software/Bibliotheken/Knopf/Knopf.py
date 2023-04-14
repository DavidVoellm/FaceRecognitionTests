import RPi.GPIO as GPIO

class Knopf:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Pin als Input festlegen; da normalerweise Knopf nicht gedückt ist: pull-down da normal kein Strom fließt
    def istGedrueckt(self): # gibt true zurück wenn Stromkreis geschlossen ist
        return GPIO.input(self.pin) == GPIO.HIGH
