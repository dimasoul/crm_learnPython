class Ticket:
    def __init__(self, text, subject, ticket_number):
        self.text = text
        self.subject = subject
        self.ticket_number = ticket_number

    def __str__(self):
        return f"Билет №{self.ticket_number}. По предмету: {self.subject}. Вопрос: {self.text}."