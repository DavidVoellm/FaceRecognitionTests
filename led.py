import RPi.GPIO as GPIO
import time

class LED_HANDLER:
    def __init__(self,rot=22,gruen=27,blau=17):
        self.setup(rot,gruen,blau)
        self.outputs = []
    def setup(self,rot=22,gruen=27,blau=17):
        self.rot = rot
        self.gruen = gruen
        self.blau = blau

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(rot,  GPIO.OUT)
        GPIO.setup(gruen,  GPIO.OUT)
        GPIO.setup(blau,  GPIO.OUT)

    def setLEDS(self,outputs):
        self.outputs = []
        GPIO.output(self.rot, outputs[0])
        GPIO.output(self.gruen, outputs[1])
        GPIO.output(self.blau, outputs[2])

    def test(self,amount=10):
        for i in range(amount):
            self.setLEDS([1,0,0])
            time.sleep(0.2)
            self.setLEDS([1,1,0])
            time.sleep(0.2)
            self.setLEDS([0,1,0])
            time.sleep(0.2)
            self.setLEDS([0,1,1])
            time.sleep(0.2)
            self.setLEDS([0,0,1])
            time.sleep(0.2)
            self.setLEDS([1,0,1])
            time.sleep(0.2)
    
    def cleanup(self):
        GPIO.cleanup()
#e4:5f:01:0b:82:f4
