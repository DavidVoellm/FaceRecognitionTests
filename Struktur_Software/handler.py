from Bibliotheken import *
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
            personen = personen_in_bild()
            if self.PersonenHandler.sind_personen_berechtigt(personen):
                oeffneTuer()
    def oeffne_tuer(self):
        pass
    def personen_in_bild(self, bild=None) -> list[str]:
        bild = self.Camera.get_frame() if bild is None else bild
        return self.Erkennung.get_face_names(bild)