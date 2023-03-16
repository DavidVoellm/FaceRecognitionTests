import imp
import os
from .PersonenHandler import Person

class PersonenHandler:
    def __init__(self):
        self.personen = []
        pass
    def find(self, dir): 
        for file in os.listdir(dir):
            if file.endswith(".jpg"):
                name = os.path.filename(file)
                self.personen.append(Person(name, file))
    def get_personen(self):
        return self.personen