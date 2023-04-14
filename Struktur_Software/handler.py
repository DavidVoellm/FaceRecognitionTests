from Bibliotheken import *
import time
class Handler: # Führt alle Notwendigen Befehle aus, aber Hauptdatei bleibt übersichtlich und kurz
    def __init__(self, Buzzer:Buzzer, LED:LED, Servo:Servo, Camera:Camera, PersonenHandler:PersonenHandler, Erkennung:Gesichtserkennung, Knopf:Knopf, Tuer:Knopf):
        self.Buzzer = Buzzer
        self.LED = LED
        self.Servo = Servo
        self.Camera = Camera
        self.PersonenHandler = PersonenHandler
        self.Erkennung = Erkennung
        self.Knopf = Knopf
        self.Tuer = Tuer

        self.tuer_zu = False
    def begin(self) -> None:
        self.LED.set([1,1,0])                   # Orangenes Licht - > Initialisiervorgang läuft
        self.Servo.setAngle(180)                # Schloss anfangs öffnen
        personen = self.PersonenHandler.find("./Daten") # Alle erlaubten Personen aus Ordner Daten laden
        self.Erkennung.set_personen(personen)   # Gesichtskodierungen für erlaubte Personen erstellen
        self.LED.set([0,1,0])                   # Grünes Licht - > Bereit & Türe offen
    def loop(self):
        if self.tuer_zu:                                # Gesichtserkennung nur bei geschlossener Tür
            if self.Knopf.istGedrueckt():               # Start der Gesichtserkennung durch drücken des Knopfes
                print("Knopf gedrückt") # Debugging Information
                self.LED.set([0,0,1])                   # Blaues Licht - > Gesichtserkennung gestartet
                while self.Knopf.istGedrueckt(): pass   # warten bis Knopf wieder losgelassen wurde, damit Gesichtserkennung nicht mehrfach direkt hintereinander läuft

                personen = self.personen_in_bild()      # Findet alle Personen im Bild der Kamera und ordnet ihnen Namen zu
                print(personen) # Debugging Information
                if self.PersonenHandler.sind_personen_berechtigt(personen): # Wenn bekannte Personen dabei sind soll die Tür aufgeschlossen werden
                    print("Tür öffnen") # Debugging Information
                    self.aufschliessen()
                    while self.Tuer.istGedrueckt():     # warten bis jemand die Tür öffnet
                        pass
                    self.tuer_zu = False

                else:                                   # Wenn Personen unbekannt sind soll die Türe verschlossen bleiben und ein Alarm läuten
                    self.LED.set([1,0,0])               # Rotes Licht - > Tür zu
                    self.Buzzer.on()
                    time.sleep(0.5)                     # Alarm für 0.5 Sekunden
                    self.Buzzer.off()
        else:
            if(self.Tuer.istGedrueckt()):               # Wenn die Türe geschlossen wird, soll der Servo wieder das Schloss vorschieben
                self.tuer_zu = True
                print("Tür schliessen") # Debugging Information
                self.zuschliessen()

            #'''Mögliche Zusatzfunktion: neues Bild aufnehmen'''

    def aufschliessen(self):
        self.LED.set([1,1,0])       # Orangenes Wartelicht
        self.Servo.setAngle(180)    # Schloss weg von der Tür drehen - > öffnen
        self.LED.set([0,1,0])       # Grünes Licht - > Tür offen
    def zuschliessen(self):
        self.LED.set([1,1,0])       # Orangenes Wartelicht
        self.Servo.setAngle(0)      # Schloss hin zu der Tür drehen - > zu
        self.LED.set([1,0,0])       # Rotes Licht - > Tür zu

    def personen_in_bild(self, bild=None) -> list[str]: # gibt alle Namen der Personenen im Bild zurück
        bild = self.Camera.get_frame() if bild is None else bild # Wenn ein Bild übergeben wurde wird das untersucht, ansonsten die Aufnahme der Kamera
        return self.Erkennung.get_face_names(bild)      # Ordnet Gesichtern im Bild Namen zu
