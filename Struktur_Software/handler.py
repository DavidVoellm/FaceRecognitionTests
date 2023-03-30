from Bibliotheken import *
import time
class Handler:
    def __init__(self, Buzzer:Buzzer, LED:LED, Servo, Camera, PersonenHandler, Erkennung, Knopf, oeffneFunc=None, schliessFunc=None):
        self.Buzzer:Buzzer = Buzzer
        self.LED:LED = LED
        self.Servo = Servo
        self.Camera = Camera
        self.PersonenHandler = PersonenHandler
        self.Erkennung = Erkennung
        self.Knopf = Knopf

        self.oeffneFunc = oeffneFunc
        self.schliessFunc = schliessFunc
    def begin(self) -> None:
        self.LED.set([1,0,0])
        self.Servo.setAngle(0)
        self.PersonenHandler.find("./Daten")
        self.Erkennung.set_personen(self.PersonenHandler.get_personen())
    def loop(self):
        if self.Knopf.istGedrueckt():
            print("Knopf gedrückt")
            personen =self. personen_in_bild()
            print(personen)
            if self.PersonenHandler.sind_personen_berechtigt(personen):
                self.oeffne_tuer()
                print("Tür öffnen")
            else:
                #in echt nicht tür schliessen bei falschem Gesicht
                self.schliesse_tuer()
                self.Buzzer.on()
                time.sleep(0.5)
                self.Buzzer.off()
                
    def oeffne_tuer(self):
        self.Servo.setAngle(180)
        self.LED.set([0,1,0])
    def schliesse_tuer(self):
        self.Servo.setAngle(0)
        self.LED.set([1,0,0])
    def personen_in_bild(self, bild=None) -> list[str]:
        bild = self.Camera.get_frame() if bild is None else bild
        return self.Erkennung.get_face_names(bild)
