import RPi.GPIO as GPIO
import time

class LED:
    def __init__(self,rot=22,gruen=27,blau=17):
        self.rot = rot
        self.gruen = gruen
        self.blau = blau

        GPIO.setup(rot,  GPIO.OUT) # benötigte Pins als Ouput festlegen
        GPIO.setup(gruen,  GPIO.OUT)
        GPIO.setup(blau,  GPIO.OUT)

        self.outputs = [] 
        self.set([0,0,0]) # Am Anfang alle ausschalten


    def set(self,outputs): # Liste Ouput hat die Länge 3 mit den Werten für Rot, Grün und Blau (Integer Werte: an oder aus, ansonsten müsste PWM funktion genutzt werden)
        if outputs == self.outpus: return # Damit Funktion nur läuft, wenn Werte sich auch geändert haben
        self.outputs = outputs # Neue Werte speichern
        GPIO.output(self.rot, outputs[0])  # Ouputwerte verändern
        GPIO.output(self.gruen, outputs[1])
        GPIO.output(self.blau, outputs[2])

    def test(self,amount=10): # Einfache Funktion zum testen der RGB
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