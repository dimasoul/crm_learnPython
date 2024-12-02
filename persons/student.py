from persons.human import Human

class Student(Human):
    MIN_AGE = 18
    MAX_AGE = 25

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.marks = {}
        self.students = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.name}, {self.age} лет"

    def get_grade(self, subject, mark):
        self.marks[subject] = mark
        print(f"{self.name} получил {mark} по {subject}")

    def show_marks(self):
        print(f"Оценки студента {self.name}:")
        for self.subject, mark in self.marks.items():
            print(f"{self.subject}: {mark}")

    def enrollment(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Оценки студента {self.name}:")

    def kick(self, student_group):
        student_group.students.remove(self)
        print(f"{self.name} отчислен(а) из группы {student_group.group_name}.")
