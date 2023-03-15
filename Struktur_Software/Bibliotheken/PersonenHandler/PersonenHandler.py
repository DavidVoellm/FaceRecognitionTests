import os
import face_recognition

class PersonenHandler:
    def __init__(self) -> None:
        self.face_encodings = []
        self.face_names = []
        pass
    def find(self, dir): 
        for file in os.listdir(dir):
            if file.endswith(".jpg"):
                encoding = self.__create_face_encoding(file)
                name = os.path.filename(file)
                self.face_encodings.append(encoding)
                self.face_names.append(name)
    def __create_face_encoding(path):
        image = face_recognition.load_image_file(path)
        face_encoding = face_recognition.face_encodings(image)[0]
        return face_encoding
    def get_face_encodings(self):
        return self.face_encodings
    def get_face_names(self):
        return self.face_names