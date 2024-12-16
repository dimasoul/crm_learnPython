from contextlib import nullcontext

from faker import Faker

from exceptions.exceptions import SchoolGroupError
from persons.student import Student
from persons.student_group import StudentGroup
from persons.teacher import Teacher
from tickets.ticket_generator import TicketGenerator
from exams.exam import Exam
from exams.subject import Subject, Object
import random

faker = Faker('ru_RU')
teacher1 = Teacher(faker.name(), faker.random_int(min=Teacher.MIN_AGE, max=Teacher.MAX_AGE), "Male")
teacher2 = Teacher(faker.name(), faker.random_int(min=Teacher.MIN_AGE, max=Teacher.MAX_AGE), "Male")
#Создаем учителей

student1 = Student(faker.name(), faker.random_int(min=Student.MIN_AGE, max=Student.MAX_AGE), "Male")
student2 = Student(faker.name(), faker.random_int(min=Student.MIN_AGE, max=Student.MAX_AGE), "Female")

sub = Subject(subject_name=Object)
subject = sub.subject_name

teacher1.teaches_subject(faker.word(ext_word_list=subject))
teacher2.teaches_subject(faker.word(ext_word_list=subject))

student1.get_grade(faker.word(ext_word_list=subject), 5)
student1.get_grade(faker.word(ext_word_list=subject), 5)
student2.get_grade(faker.word(ext_word_list=subject), 4)

teacher1.teaching_student(student1, faker.word(ext_word_list=subject))
teacher2.teaching_student(student2, faker.word(ext_word_list=subject))

student1.show_marks()
student2.show_marks()

students_first = [Student(faker.name(), faker.random_int(min=Student.MIN_AGE, max=Student.MAX_AGE), "Male") for _ in range(10)]
students_second = [Student(faker.name(), faker.random_int(min=Student.MIN_AGE, max=Student.MAX_AGE), "Male") for _ in range(15)]
students_th = [Student(faker.name(), faker.random_int(min=Student.MIN_AGE, max=Student.MAX_AGE), "Male") for _ in range(0)]

sg1 = StudentGroup(faker.bothify(letters=StudentGroup.LETTERS),students=students_first)
sg2 = StudentGroup(faker.bothify(letters=StudentGroup.LETTERS),students=students_second)
sg3 = StudentGroup(faker.bothify(letters=StudentGroup.LETTERS),students=students_th)

for student in students_first:
    student.enroll(sg1)

#Студента1 Зачислили в Группу1
sg1.add_student(student1)

for student in sg1:
    print(student)

for student in sg2:
    print(student)

#Создаем экзамены для двух разных групп
exam1 = Exam(faker.word(ext_word_list=subject), sg1, faker.date(), faker.date())
exam2 = Exam(faker.word(ext_word_list=subject), sg2, faker.date(), faker.date())

#Учителя проводят экзамен
teacher1.conduct_exam(exam1)
teacher2.conduct_exam(exam2)

#Студента отчислили из Группы1
student1.kick()

#Первой группе начислили стипендию
sg1.pay_all()

#Уведомление о начале экзамена во второй группе
sg2.notify()

sg1.kick_all()

#Генерируем билеты
tg = TicketGenerator(teacher1, exam1.subject, sg1)
obj1 = tg.get_ticket(len(sg1.students))
for o in obj1:
    print(o)

#Сравниваем группы
print(sg1 == sg2)

#Генерируем билетов меньше чем количество учеников в группе
tg = TicketGenerator(teacher2, exam1.subject, sg2)
obj2 = tg.get_ticket(len(sg2.students))
for o in obj2:
    print(o)

print(sg1 == sg2)

sg3.pay_all()

#Генерируем билетов для группы в которой нет студентов
tg = TicketGenerator(teacher2, exam1.subject, sg3)

while True:
    try:
        for ticket in tg.get_ticket(len(sg3.students)):
            print(ticket)
    except ValueError as err:
        if str(err) == "Максимальное количество билетов превышено":
            continue
        else:
            raise err
    break

