from faker import Faker

from exceptions.exceptions import SchoolGroupError
from tickets.ticket import Ticket

faker = Faker('ru_RU')

class TicketGenerator:
    def __init__(self, teacher, subject, student_group):
        self.teacher = teacher
        self.subject = subject
        self.student_group = student_group
        self.MAX_TICKET_COUNT = 16

    def get_ticket(self, n):
        if n < 0:
            raise ValueError("n не может быть меньше 0.")
        elif n >= self.MAX_TICKET_COUNT:
            raise ValueError("Максимальное количество билетов превышено")
        elif n == 0:
            raise ValueError("Студенты в группе отсутствуют, генерация билетов невозможна.")
        for ticket in range(n):
            yield Ticket(faker.sentence(), self.subject, ticket)
