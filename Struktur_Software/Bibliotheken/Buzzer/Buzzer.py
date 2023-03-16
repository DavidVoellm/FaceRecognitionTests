import RPi.GPIO as GPIO

class Buzzer:
    def __init__(self, pin=20, defaultFrequency=1000):
        self.pin = pin
        GPIO.setup(pin,GPIO.OUT)
        self.defaultFrequency = defaultFrequency
        self.buzzer = GPIO.PWM(pin, defaultFrequency)
        self.buzzer.start(0)
    def setFrequency(self,frequency):
        if self.defaultFrequency != frequency:
            self.defaultFrequency = frequency
            self.buzzer.ChangeFrequency(frequency)
    def off(self):
        self.buzzer.ChangeDutyCycle(0)
    def on(self):
        self.buzzer.ChangeDutyCycle(1)
    def stop(self):
        self.buzzer.stop()