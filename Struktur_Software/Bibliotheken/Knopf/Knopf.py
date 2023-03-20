import RPi.GPIO as GPIO

class Knopf:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    def istGedrueckt(self):
        return GPIO.input(self.pin) == GPIO.HIGH
