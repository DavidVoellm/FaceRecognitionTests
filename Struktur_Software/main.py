from .Bibliotheken import *
import os

personen_handler = PersonenHandler()
camera = Camera()
erkennung = Gesichtserkennung()
personen_handler.find("./Daten")

erkennung.set_personen(personen_handler.get_personen())

unknown_image = camera.get_frame_as_array()

names = erkennung.get_face_names(unknown_image)