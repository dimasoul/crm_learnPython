from faker import Faker

from exceptions.exceptions import SchoolGroupError
from tickets.ticket import Ticket

faker = Faker('ru_RU')

class TicketGenerator:
    def __init__(self, teacher, subject, student_group):
        self.teacher = teacher
        self.subject = subject
        self.student_group = student_group

    def get_ticket(self, n):
        if 0 < n < 15:
            for ticket in range(n):
                yield Ticket(faker.sentence(), self.subject, ticket)
        elif n == 0:
            raise ValueError("Студенты в группе отсутствуют, генерация билетов невозмоэжна")
        elif n >= 16:
            raise ValueError("Максимальное количество билетов превышено")
