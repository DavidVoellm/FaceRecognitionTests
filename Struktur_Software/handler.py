from Bibliotheken import *
class Handler:
    def __init__(self, LED:LED, Servo, Camera, PersonenHandler, Erkennung, oeffneFunc=None, schliessFunc=None):
        self.LED:LED = LED
        self.Servo = Servo
        self.Camera = Camera
        self.PersonenHandler = PersonenHandler
        self.Erkennung = Erkennung

        self.oeffneFunc = oeffneFunc
        self.schliessFunc = schliessFunc
    def begin(self) -> None:
        self.LED.set([1,0,0])
        self.Servo.setAngle(0)
        self.PersonenHandler.find("./Daten")
        self.Erkennung.set_personen(self.PersonenHandler.get_personen())

    def PersonenInBild(self, bild=None) -> list[str]:
        bild = self.Camera.get_frame() if bild is None else bild
        return self.Erkennung.get_face_names(bild)