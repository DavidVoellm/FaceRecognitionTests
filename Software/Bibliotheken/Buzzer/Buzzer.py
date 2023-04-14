import RPi.GPIO as GPIO

class Buzzer:
    def __init__(self, pin=20, defaultFrequency=1000):
        self.pin = pin
        GPIO.setup(pin,GPIO.OUT) # pin als Output festlegen
        self.defaultFrequency = defaultFrequency
        self.buzzer = GPIO.PWM(pin, defaultFrequency) # Frequenz des zu erzeugenden Tons
        self.buzzer.start(0)
    def setFrequency(self,frequency):
        if self.defaultFrequency != frequency:
            self.defaultFrequency = frequency
            self.buzzer.ChangeFrequency(frequency)
    def off(self):
        self.buzzer.ChangeDutyCycle(0) # Wenn Puls-Weiten-Modulation = 0% ist, dann kommt kein Signal mehr durch -> aus
    def on(self):
        self.buzzer.ChangeDutyCycle(50)
    def stop(self):
        self.buzzer.stop() # macht PWM wieder aus