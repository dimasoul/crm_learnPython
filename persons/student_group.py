class StudentGroup:
    LETTERS = 'ABCDE'

    def __init__(self, group_name, students: list):
        self.group_name = group_name
        self.students = students

    def __str__(self):
        return self.group_name

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


    def __len__(self):
        return len(self.students)

    def __contains__(self, item):
        return item in self.students

    def __eq__(self, other):
        return self.group_name == other.group_name and self.students == other.students

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} зачислен в группу {self.group_name}")

    def remove_student(self, student):
        self.students.remove(student)
        print(f"{student.name} отчислен из группы {self.group_name}.")

    def kick_all(self):
        """Отчисление всей группы"""
        for student in self.students:
            student.kick()
            print(f" Все студенты отчислены из группы {self.group_name}.")

    def pay_all(self):
        """Начисление стипендии всей группе"""
        for student in self.students:
            print(f"Студенту {student} из группы {self.group_name}. начислена стипендия")

    def notify(self):
        """Уведомление группы студентов"""
        print(f" Уведомление о начале экзамена для группы {self.group_name}.")
