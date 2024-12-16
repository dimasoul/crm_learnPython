from persons.human import Human

class Student(Human):
    MIN_AGE = 18
    MAX_AGE = 25

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.marks = {}
        self.group = None

    def __str__(self):
        return f"{self.name}, {self.age} лет"

    def get_grade(self, subject, mark):
        print(f"{self.name} получил {mark} по {subject}")
        self.marks[subject] = mark

    def show_marks(self):
        print(f"Оценки студента {self.name}:")
        for self.subject, mark in self.marks.items():
            print(f"{self.subject}: {mark}")

    def enroll(self, group):
        self.group = group
        group.add_student(self)

    def kick(self):
        if self.group is not None:
            print(f"{self.name} отчислен из группы {self.group.group_name}.")
            self.group.remove_student(self)
            self.group = None
        else:
            print(f"{self.name} не состоит в группе.")
