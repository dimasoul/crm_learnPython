from persons.human import Human
import random

class Teacher(Human):
    MIN_AGE = 25
    MAX_AGE = 55

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.subjects = []

    def teaches_subject(self, subject):
        self.subjects.append(subject)
        for self.subject in self.subjects:
            print(f"{self.name} преподает {self.subject}")

    def teaching_student(self, student, subject):
        if subject in self.subjects:
            print(f"{self.name} учит {student.name} {subject}")
        else:
            print(f"{self.name} не преподает предмет {subject}.")

    def conduct_exam(self, exam):
        print(f"{self.name} проводит экзамен по предмету {exam.subject} для группы {exam.student_group}, который начинается {exam.date_start}")

    def get_subject(self):
        return random.choice(self.subjects)
