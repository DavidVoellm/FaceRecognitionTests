import cv2
import numpy

class Camera:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_AUTOFOCUS, 1)
    def __del__(self):
        self.cam.release()
    def get_frame(self): 
        _, frame = self.cam.read()
        return frame
    def get_frame_as_array(self): 
        _, frame = self.cam.read()
        return numpy.asarray(frame)