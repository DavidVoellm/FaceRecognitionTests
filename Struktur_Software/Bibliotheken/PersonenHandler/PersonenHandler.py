import os
from .Person import Person

class PersonenHandler:
    def __init__(self):
        self.personen = []
    def find(self, dir): 
        for file in os.listdir(dir):
            if file.endswith(".jpg"):
                name = file[:-4]
                self.personen.append(Person(name, dir+"/"+file))
    def get_personen(self):
        return self.personen
    def sind_personen_berechtigt(self, names):
        for person in self.personen:
            for name in names:
                if person.name == name:
                    return True
        return False
