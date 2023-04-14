import face_recognition
import numpy as np

class Gesichtserkennung:
    def __init__(self):
        self.face_encodings = []
        self.face_names = []
    def __create_face_encoding(path): # aus Pfad zu Bild eine Kodierung zur Wiedererkennung des Gesichts erstellen
        image = face_recognition.load_image_file(path) # Bild laden
        face_encoding = face_recognition.face_encodings(image)[0] # Kodierung erstellen
        return face_encoding
    def set_personen(self, personen): # für eine Liste von Personen jeweils eine Kodierung erstellen und alle merken
        for person in personen:
            encoding = Gesichtserkennung.__create_face_encoding(person.image) # Eigene Funktion von oben nutzen um aus dem Pfad zum Bild ein wiedererkennbares Gesicht zu machen
            self.face_encodings.append(encoding) # Kodierung zur Liste von Kodierungen hinzufügen
            self.face_names.append(person.name) # Name zur Namensliste hinzufügen
    def get_face_names(self, unknown_image):
        names = []
        face_locations = face_recognition.face_locations(unknown_image) # Alle Gesichter in unbekanntem Bild finden
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations) # Gesichter wieder in vergleichbare Kodierung umwandeln
        for face_encoding in face_encodings: # Alle gefundenen Gesichter einzeln untersuchen
            matches = face_recognition.compare_faces(self.face_encodings, face_encoding, 0.6) # passt gefundenes Gesicht zu bekannten Gesichtern, mit Toleranz 0.6 (je kleiner desto genauer)
            name = "Unknown" # Falls Gesicht unbekannt bleibt soll es nachher mit dem Name "Unknown" versehen werden
            face_distances = face_recognition.face_distance(self.face_encodings, face_encoding) # Gibt für jedes bekannte Gesicht an, wie gut es zu dem gefundenen passt
            best_match_index = np.argmin(face_distances) # gibt den Index an, für das bekannte Gesicht, welches am besten passt
            if matches[best_match_index]: # Wenn das am ähnlichste Gesicht passt
                name = self.face_names[best_match_index] # soll der Name des bekannten Gesichts für das unbekannte verwendet werden
            names.append(name)
        return names