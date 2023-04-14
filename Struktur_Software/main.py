from handler import Handler
from Bibliotheken import * # Importiert alle Bibliotheken aus dem Ordner Bibliotheken

GPIO.setmode(GPIO.BCM) # Damit wird nur festgelegt wie die Ports nummeriert werden (in diesem Fall wie in pinBelegung.png in den orangenen Kästen)

# Handler Objekt wird erstellt und Pins der einzelnen Bauteile können definiert werden
handler = Handler(Buzzer(pin=20), LED(rot=22, gruen=23,blau=24), Servo(pin=17), Camera(0), PersonenHandler(),Gesichtserkennung(), Knopf(pin=5), Knopf(pin=6)) 
# Handler Initialisiert alles nötige
handler.begin()

print("ready") # Debugging Information

try: # Falls ein Fehler auftritt oder das Programm bewusst unterbrochen wird stürzt das Programm nicht ab
    while True: # Programm soll fortlaufen wiederholt werden
        handler.loop() # Hauptschleife des Handlers wird aufgerufen
except Exception as e:
    print('Error', str(e)) # Fehlerausgabe

GPIO.cleanup() # Falls das Programm beendet wurde oder ein Fehler auf kommt werden die Ports freigegeben und können direkt wieder genutzt werden