'''Datei zum testen der Gesichtserkunnungsfunktion'''
from Bibliotheken import *
import cv2

personen_handler = PersonenHandler()
camera = Camera()
erkennung = Gesichtserkennung()
personen = personen_handler.find("./Daten")

erkennung.set_personen(personen) # Kodierung für bekannte Gesichter erstellen

frame = camera.get_frame() # Bild mit Kamera aufnehmen
cv2.imwrite("./frame.jpg", frame) # Zum späteren überprüfen und Kamera testen Bild abspeichern

berechtigtePersonenImBild = erkennung.get_face_names(frame) # Personen im Bild erkennen und ihnen Namen zuordnen
print(berechtigtePersonenImBild)