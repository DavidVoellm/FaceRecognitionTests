from Bibliotheken import *
import time
from datetime import datetime

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
                    while self.Tuer.istGedrueckt(): # warten bis jemand die Tür öffnet
                        #'''Mögliche Zusatzfunktion: neue Person aufnehmen'''
                        erg = self.neue_person_hinzufuegen()
                        if erg is False or erg is True:
                            self.LED.set([0,0,1])   
                            break
                    
                    time.sleep(1)                       # noch eine extra Sekunde warten, damit nicht durch einen Wackelkontakt an der Kontaktschleife die Türe sofort wieder verschlossen wird
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
    
    def get_time(self):
        return datetime.strptime( datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")
    def warten_mit_abbruch(self, time): # wartet 'time' Sekunden und gibt False zurück wenn Knopf zwischen drin gedrückt wurde
        start_time = self.get_time() # speichert aktuelle Zeit
        current_time = start_time
        while not self.Knopf.istGedrueckt():
            current_time = self.get_time()
            if (current_time-start_time).total_seconds()>=time: # Abfrage ob Knopf für mindestens 'time' Sekunden nicht gedrückt wurde
                return True
        return False

    def neue_person_hinzufuegen(self):
        if self.Knopf.istGedrueckt():               # Neues Gesicht bei Knopfdruck hinzufügen
            start_time = self.get_time() # speichert aktuelle Zeit
            current_time = start_time
            while self.Knopf.istGedrueckt():
                current_time = self.get_time()
                if (current_time-start_time).total_seconds()>=2: # Abfrage ob Knopf für mindestens 2 Sekunden gedrückt wurde
                    self.LED.set([0,0,1])                   # blaues Licht -> neues Gesicht kann hinzugefügt werden
            if (current_time-start_time).total_seconds()<2: return None # wenn Knopf für weniger als 2 Sekunden gedrückt wurde soll abgebrochen werden
            self.LED.set([0,0,1])                               # blaues Blinklicht -> in 1,6 sekunden wird Bild aufgenommen, kann mit Knopfdruck abgebrochen werden
            if not self.warten_mit_abbruch(0.5): return False
            self.LED.set([0,0,0]) 
            if not self.warten_mit_abbruch(0.3): return False
            self.LED.set([0,0,1]) 
            if not self.warten_mit_abbruch(0.5): return False
            self.LED.set([0,0,0]) 
            if not self.warten_mit_abbruch(0.3): return False
            self.LED.set([1,1,1]) 
            while not self.Knopf.istGedrueckt():
                one_person, encoding = self.Erkennung.is_one_new_face(self.Camera.get_frame()) # Im Bild der Kamera nach neuer Person suchen
                if one_person: # Wenn genau eine neue Person dabei ist
                    name = self.Erkennung.add_person(encoding) # Person zu bekannten Personen hinzufügen
                    self.PersonenHandler.add(name) # Person zu erlaubten Personen hinzufügen
                    print("Person hinzugefügt")
                    return True
                if not self.warten_mit_abbruch(0.3): return False
            return False
    
    def end(self):
        self.LED.set([0,0,0]) # LED wieder ausschalten
        GPIO.cleanup() # Falls das Programm beendet wurde oder ein Fehler auf kommt werden die Ports freigegeben und können direkt wieder genutzt werden