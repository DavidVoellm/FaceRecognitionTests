import cv2
from Bibliotheken import Camera
camera = Camera()
frame = camera.get_frame() # Bild mit Kamera aufnehmen
cv2.imwrite("./frame.jpg", frame) # Zum späteren überprüfen und Kamera testen Bild abspeichern