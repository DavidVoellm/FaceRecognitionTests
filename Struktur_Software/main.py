from handler import Handler
from Bibliotheken import *

handler = Handler(LED(rot=22, gruen=23,blau=24), Servo(pin=17), Camera(0), PersonenHandler(),Gesichtserkennung())
handler.begin()
handler.PersonenInBild()

while True:
    pass
    if None():
        pass