# House with Security-Door and FaceRecognition
Controle door lock with Raspberry Pi and camera, so it only opens if the right person is in front.

## Used Components
 - Raspberry Pi 3b+
 - Camera (type unknown)
 - RGB LED
 - Servo Motor
 - 2 Buttons
 - Buzzer
 - Fan



## Facerecognition

[FaceRecognition lib](https://github.com/ageitgey/face_recognition) for python

[dlib](http://dlib.net/python/index.html) for FaceRecognition to work

Code inspiration from [bradtraversy](https://github.com/bradtraversy/face_recognition_examples/blob/master/indentify.py)

## TODO
 - Buzzer programmierung
 - Schaniere
 - Platine (Buzzer, LED, Servo, Knopf)
 - Hauptklasse zum Programmhandling: warten auf Knopf, auf, zu, ...
 - einbau dieser Klasse in main.py
 - Buzzer Gehäuse
 - LED Gehäuse