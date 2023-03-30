from handler import Handler
from Bibliotheken import *

GPIO.setmode(GPIO.BCM)

handler = Handler(Buzzer(pin=20), LED(rot=22, gruen=23,blau=24), Servo(pin=17), Camera(0), PersonenHandler(),Gesichtserkennung(), Knopf(pin=5))
handler.begin()
#print(handler.personen_in_bild())

print("ready")
try:
    while True:
        handler.loop()
except Exception as e:
    print('Error', str(e))
    raise
