import os
from .Person import Person

class PersonenHandler:
    def __init__(self):
        self.personen = []
        pass
    def find(self, dir): 
        for file in os.listdir(dir):
            print(dir) # Debug
            if file.endswith(".jpg"):
                name = file[:-4]
                self.personen.append(Person(name, dir+file))
    def get_personen(self):
        return self.personen