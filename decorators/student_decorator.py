class StudentDecorator:
    """Декоратор для студента, добавляющий пометку 'староста'."""

    def __init__(self, student):
        self.student = student

    @property
    def name(self):
        return self.student.name

    def __str__(self):
        return f"{self.student.name} (староста)"