from handler import Handler
from Bibliotheken import *

GPIO.setmode(GPIO.BCM)

handler = Handler(Buzzer(pin=20), LED(rot=22, gruen=23,blau=24), Servo(pin=17), Camera(0), PersonenHandler(),Gesichtserkennung())
handler.begin()
print(handler.PersonenInBild())


while True:
    break