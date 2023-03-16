import face_recognition
import numpy as np

class Gesichtserkennung:
    def __init__(self):
        self.face_encodings = []
        self.face_names = []
    def __create_face_encoding(path):
        image = face_recognition.load_image_file(path)
        face_encoding = face_recognition.face_encodings(image)[0]
        return face_encoding
    def set_personen(self, personen):
        for person in personen:
            encoding = self.__create_face_encoding(person.image)
            self.face_encodings.append(encoding)
            self.face_names.append(person.name)
        pass
    def get_face_names(self, unknown_image):
        names = []
        for face_encoding in self.face_encodings:
            matches = face_recognition.compare_faces(self.face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(self.face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.face_names[best_match_index]
            names.append(name)
        return names