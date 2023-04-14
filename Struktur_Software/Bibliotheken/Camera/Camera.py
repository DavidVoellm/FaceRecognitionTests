import cv2

class Camera:
    def __init__(self, cam:int=0):
        self.cam = cv2.VideoCapture(cam) # Mit open cv Kamera finden und nutzen
    def __del__(self):
        self.cam.release()
    def get_frame(self): # "Foto" aufnehmen
        _, frame = self.cam.read()
        return frame