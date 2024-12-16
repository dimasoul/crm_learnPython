from enum import StrEnum
import random

class Object(StrEnum):
    GEOM = "Геометрия"
    MATH = "Математика"
    ENG = "Английский"
    PHIS = "Физика"
    ROBO = "Робототехника"
    ELECTRO = "Электроника"

# current_subject = [Subjects.GEOM, Subjects.MATH, Subjects.ENG, Subjects.PHIS, Subjects.ROBO, Subjects.ELECTRO]

class Subject:
    def __init__(self, subject_name: Object):
        self.subject_name = subject_name

    def __str__(self):
        return self.subject_name

