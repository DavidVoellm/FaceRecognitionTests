import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self, pin, frequency = 50):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT) # Pin als Output festlegen
        self.p = GPIO.PWM(pin, frequency) # PWM Objekt erstellen um Servo zu steuern
        self.p.start(0)
    def setAngle(self, angle:float): # Servo in gewünschten Winkel ausrichten
        pos = 2+(angle/18) # Durch Recherche und ausprobieren herausgefunden: dadurch dreht sich der Servo genau auf den gewünschten Winkel
        self.p.ChangeDutyCycle(pos)
        time.sleep(0.5)
        self.p.ChangeDutyCycle(0)
    def stop(self):
        self.p.stop()

