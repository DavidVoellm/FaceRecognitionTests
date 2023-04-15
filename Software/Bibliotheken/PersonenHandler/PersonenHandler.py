import os
from .Person import Person

class PersonenHandler:
    def __init__(self):
        self.personen = []
    def find(self, dir): # findet in gegebenem Pfad alle Bilder und erstellt aus der Benennung den dazugehörigen Namen
        for file in os.listdir(dir):  # Geht durch jede Datei in gegebenem Ordner
            if file.endswith(".jpg"): # Falls der Dateiname mit -jpg endet
                name = file[:-4] # Name ist der Dateiname ohne die ".jpg"-Endung
                self.personen.append(Person(name, dir+"/"+file)) # Person wird Liste hinzugefügt
        return self.personen
    def add(self, name):
        self.personen.append(Person(name, ""))
    def sind_personen_berechtigt(self, names): # gibt True zurück wenn mindestens einer der Namen in der gespeicherten Namensliste vorkommt
        for person in self.personen:
            for name in names:
                if person.name == name:
                    return True
        return False