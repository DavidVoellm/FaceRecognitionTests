import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self, pin, frequency = 50):
        self.pin = pin
        self.frequency = frequency
        GPIO.setup(pin, GPIO.OUT)
        self.p = GPIO.PWM(pin, 50)
        self.p.start(0)
    def setAngle(self, angle:float):
        pos = 2+(angle/18)
        self.p.ChangeDutyCycle(pos)
        time.sleep(0.5)
        self.p.ChangeDutyCycle(0)
    def stop(self):
        self.p.stop()

